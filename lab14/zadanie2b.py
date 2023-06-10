import socket
import ssl

server_address = 'httpbin.org'
port = 443


req = 'GET /html HTTP/1.1 \r\n' \
      'Host: httpbin.org\r\n' \
      'User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A\r\n\r\n'


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
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ssl_socket = ssl.wrap_socket(client_socket)

    try:
        file = open("zadanie2b.html", "w")

        ssl_socket.connect((server_address, port))
        ssl_socket.sendall(req.encode('utf-8'))

        headers = receive_headers(ssl_socket).split('\r\n')

        content_length = 0

        for header in headers:
            if 'Content-Length' in header:
                content_length = int(header.split(': ')[1])

        html = receive_body(ssl_socket, content_length).decode('utf-8')

        file.write(html)
        file.close()

    except socket.error as e:
        print('Error occurred while connecting to server: {}'.format(e))

    ssl_socket.close()
