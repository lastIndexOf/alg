from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        content = '<h1>hello %s</h1>' % self.path
        if self.path == '/':
            self.wfile.write(content.encode())
        else:
            self.wfile.write(content.encode())


if __name__ == '__main__':
    port = 9003
    host = ('', port)
    server = ThreadingHTTPServer(host, HttpHandler)

    print('server run at http://127.0.0.1:%d' % port)
    server.serve_forever()
