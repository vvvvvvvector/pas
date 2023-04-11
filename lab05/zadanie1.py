import socket

server_address = ('127.0.0.1', 2965)


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server")

        data = ""

        while data != "exit":
            data = input("Enter data to send to the server: ")
            my_socket.send(data.encode('utf-8'))

            server_answer = my_socket.recv(1024).decode('utf-8')
            print(server_answer)

            if server_answer == "You win!":
                print("Server was turned off")
                break

    else:
        print('Connection failed')

    my_socket.close()
    print("Connection closed on client side")


if __name__ == '__main__':
    client_program()
