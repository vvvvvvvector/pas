import socket

server_address = ('212.182.24.236', 2902)


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.settimeout(5.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server")

        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")
        operation = input("Enter operation: ")

        my_socket.send(first_number.encode('utf-8'))
        my_socket.send(second_number.encode('utf-8'))
        my_socket.send(operation.encode('utf-8'))

        server_answer = my_socket.recv(1024).decode('utf-8')

        print(server_answer)

    else:
        print('Connection failed')

    my_socket.close()
    print("Connection closed on client side")


if __name__ == '__main__':
    client_program()
