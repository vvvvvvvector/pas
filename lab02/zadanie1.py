import socket

server_address = ('ntp.task.gda.pl', 13)

if __name__ == '__main__':
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print('Successfully connected')
        date = my_socket.recv(1024)  # receive a message from a socket
        print(date)

    else:
        print('Connection failed')

    my_socket.close()
