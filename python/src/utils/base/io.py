from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


class Handler(Thread):
    def __init__(self, sock):
        super().__init__()

        self.__sock = sock

    def run(self):
        assert self.__sock != None, '/'

        while True:
            data = self.__sock.recv(1024)

            if not data:
                print('Byte')
                break

            self.__sock.send(data)

        self.__sock.close()


def main():
    HOST = ''
    PORT = 1987
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, 1987))
    server.listen(19)

    while True:
        sock, addr = server.accept()

        print('Connected to :', addr[0], ':', addr[1])
        Handler(sock).start()

    server.close()


if __name__ == '__main__':
    main()
