import socket

host = "127.0.0.1"
port = 2906


def udp_server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))

    print(f"Server started on {host}:{port}")

    while True:
        message, address = server_socket.recvfrom(1024)

        data = message.decode('utf-8')

        if not data:
            break

        print(f"Message from {address}: {data}")

        answer = f"Hostname for the {data} is: {socket.gethostbyaddr(data)[0]}"

        server_socket.sendto(answer.encode('utf-8'), address)


if __name__ == "__main__":
    udp_server_program()
