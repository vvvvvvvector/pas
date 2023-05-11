import socket

address = 'httpbin.org'
port = 80


req = 'GET /image/png HTTP/1.1 \r\n' \
      'Host: httpbin.org\r\n' \
      'User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15\r\n\r\n'


def receive_headers(socket):
    buffer = b''
    while b'\r\n\r\n' not in buffer:
        buffer += socket.recv(1)
    return buffer.decode('utf-8')


def receive_body(socket, content_length):
    body = b''
    while len(body) < content_length:
        body += socket.recv(1)
    return body


if __name__ == '__main__':
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        file = open('zadanie2.png', 'wb')

        socket.connect((address, port))
        socket.sendall(req.encode('utf-8'))

        headers = receive_headers(socket).split('\r\n')

        content_length = 0

        for header in headers:
            if 'Content-Length' in header:
                content_length = int(header.split(': ')[1])

        image = receive_body(socket, content_length)

        file.write(image)
        file.close()

    except socket.error as e:
        print('Error occurred while connecting to server: {}'.format(e))

    socket.close()
