import socket

host = "127.0.0.1"
port = 2901


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))

    print(f"Server started on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)

        if not data:
            break

        ip_address = data.decode()

        answer = ""

        try:
            answer = f"Hostname for the {ip_address} is: {socket.gethostbyaddr(ip_address)[0]}"

        except socket.herror:
            answer = f"Hostname for the {ip_address} is not found"

        server_socket.sendto(answer.encode(), client_address)

    server_socket.close()

    print("Connection closed on server side")


if __name__ == "__main__":
    server_program()
