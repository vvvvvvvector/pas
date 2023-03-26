import socket

server_address = ('127.0.0.1', 2901)


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server")

        message = ""

        while message != "exit":
            message = input("Enter your message: ")

            my_socket.send(message.encode())

            server_answer = my_socket.recv(1024).decode()

            print(server_answer)

    else:
        print('Connection failed')

    my_socket.close()
    print("Connection closed on client side")


if __name__ == '__main__':
    client_program()
