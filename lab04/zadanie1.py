import socket

from datetime import datetime

host = '127.0.0.1'
port = 2900


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(10)  # max number of connections

    print(f"Server started on {host}:{port}")

    while True:
        client_connected, client_address = server_socket.accept()  # accept new connection

        print("Connection from: " + str(client_address))

        while True:
            data = client_connected.recv(1024).decode()

            if not data:
                print(f"Connection {client_address} was closed on client side")
                break

            now = datetime.now()
            server_answer = "Actual date and time: " + \
                now.strftime("%d/%m/%Y %H:%M:%S")

            client_connected.send(server_answer.encode())

        client_connected.close()  # close the connection


if __name__ == "__main__":
    server_program()
