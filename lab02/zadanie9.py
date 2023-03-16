import socket

server_address = ('127.0.0.1', 2906)


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.settimeout(5.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server")

        ip = input("Enter IP address: ")

        my_socket.send(ip.encode('utf-8'))

        server_answer = my_socket.recv(1024).decode('utf-8')

        print(server_answer)

    else:
        print('Connection failed')

    my_socket.close()
    print("Connection closed on client side")


if __name__ == '__main__':
    client_program()
