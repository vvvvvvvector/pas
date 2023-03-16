import socket

server_address = ('127.0.0.1', 2900)


def format_message(message):
    if len(message) < 20:
        while len(message) < 20:
            message += " "
    elif len(message) > 20:
        message = message[:20]
    return message


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server")

        message = input("Write your message: ")
        message = format_message(message)

        server_answer = my_socket.recv(20).decode('utf-8')
        print(server_answer)

    else:
        print('Connection failed')

    my_socket.close()
    print("Connection closed on client side")


if __name__ == '__main__':
    client_program()
