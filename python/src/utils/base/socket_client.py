from socket import socket

client = socket()
client.connect(('', 1987))

while True:
    raw = input('please input: ')
    client.send(raw.encode())

    if not raw:
        break

    data = client.recv(1024)
    print(data)

client.close()
