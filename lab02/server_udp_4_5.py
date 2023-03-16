import socket

host = "127.0.0.1"
port = 2901


def udp_server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))

    print(f"Server started on {host}:{port}")

    while True:
        message, address = server_socket.recvfrom(1024)

        print(f"Message from {address}: {message.decode('utf-8')}")

        answer = f"Thanks for sending: {message.decode('utf-8').upper()} in lower case"

        server_socket.sendto(answer.encode('utf-8'), address)


if __name__ == "__main__":
    udp_server_program()
