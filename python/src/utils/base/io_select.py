from threading import Thread, RLock
from socket import socket, AF_INET, SOCK_STREAM
from select import select


class Handler(Thread):
    def __init__(self):
        super().__init__()

        self.__socks = {}
        self.__lock = RLock()

    def add_sock(self, sock):
        self.__lock.acquire()
        self.__socks[sock] = sock
        self.__lock.release()

    def remove_sock(self, sock):
        self.__lock.acquire()
        self.__socks.pop(sock)
        self.__lock.release()

    def run(self):
        while True:
            _, socks, _ = select([], self.__socks.values(), [], 1)

            for sock in socks:
                data = sock.recv(1024)

                if not data:
                    print('Byte')
                    self.remove_sock(sock)
                    sock.close()
                    continue

                sock.send(data)


def main():
    HOST = ''
    PORT = 1987
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, 1987))
    server.listen(19)

    handler = Handler()
    handler.start()

    while True:
        sock, addr = server.accept()

        print('Connected to :', addr[0], ':', addr[1])
        handler.add_sock(sock)

    server.close()


if __name__ == '__main__':
    main()
