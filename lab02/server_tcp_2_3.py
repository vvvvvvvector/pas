import socket

host = '127.0.0.1'
port = 2900


def tcp_server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(10)  # max number of connections

    print(f"Server started on {host}:{port}")

    while True:
        client_connected, client_address = server_socket.accept()  # accept new connection

        # print the address of the user that just connected
        print("Connection from: " + str(client_address))

        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = client_connected.recv(1024).decode()

            if not data:
                break

            print("From connected user: " + str(data))

            server_answer = "Answer from server: " + str(data).upper()
            # send data to the client
            client_connected.send(server_answer.encode())

        client_connected.close()  # close the connection
        print("Connection closed on server side")


if __name__ == '__main__':
    tcp_server_program()
