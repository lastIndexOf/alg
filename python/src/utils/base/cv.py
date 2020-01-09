import os
import cv2
import time
import struct
import threading
from http.server import HTTPServer, ThreadingHTTPServer, BaseHTTPRequestHandler
from socketserver import TCPServer, ThreadingTCPServer
from threading import Thread, RLock
from concurrent.futures import ThreadPoolExecutor
from select import select

SIGNED_INT_MAX = 0x7FFFFFFF


class JpegStreamer(Thread):

    def __init__(self, camera):
        super().__init__()
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw  # 这是一个字典 { pr: pw }
        self.lock.release()
        return pr

    def unregister(self, pr):
        self.lock.acquire()
        self.pipes.pop(pr)
        self.lock.release()

    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ret, data = cv2.imencode(
                    '.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.tostring()

    def send(self, frame):
        n = struct.pack('L', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _, pipes, _ = select([], self.pipes.values(), [], 1)
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send(frame)


class JpegRetriever(object):

    def __init__(self, streamer):
        self.streamer = streamer

    def __enter__(self):
        streamer = self.streamer
        self.pipe = streamer.register()
        return self.retrieve()

    def __exit__(self, *args):
        self.cleanup()
        print('exit retriever')
        return True

    def retrieve(self):
        while True:
            ns = os.read(self.pipe, 8)
            n = struct.unpack('L', ns)[0]
            print('retrieve n = %d' % n)
            if n > SIGNED_INT_MAX:
                part1 = os.read(self.pipe, SIGNED_INT_MAX)
                part2 = os.read(self.pipe, n - SIGNED_INT_MAX)
                data = ''.join([part1, part2])
            else:
                data = os.read(self.pipe, n)
            yield data

    def cleanup(self):
        self.streamer.unregister(self.pipe)


class Handler(BaseHTTPRequestHandler):
    @staticmethod
    def setJpegStreamer(streamer):
        Handler.streamer = streamer

    def do_GET(self):
        with JpegRetriever(Handler.streamer) as frames:
            if not frames:
                raise TypeError()

            if self.path != '/':
                return
            self.send_response(200)
            self.send_header(
                "Content-type", 'multipart/x-mixed-replace;boundary=abcde')
            self.end_headers()

            for frame in frames:
                print('do_GET frame size: %d' % len(frame))
                self.send_frame(frame)

    def send_frame(self, frame):
        self.wfile.write(b'--abcde\r\n')
        self.wfile.write(b'Content-Type: image/jpeg\r\n')
        self.wfile.write(b'Content-Length: %d\r\n\r\n' % len(frame))
        self.wfile.write(frame)


class ThreadPoolHttpServer(ThreadingHTTPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True, max_thread=100):
        super().__init__(server_address, RequestHandlerClass)
        self.__pool = ThreadPoolExecutor(max_thread)

    def process_request(self, request, client_address):
        self.__pool.submit(self.process_request_thread,
                           request, client_address)


if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()

    Handler.setJpegStreamer(streamer)

    print('Start server ...')
    server = ThreadPoolHttpServer(('', 9010), Handler, max_thread=3)
    server.serve_forever()
