import socket

server_address = ('127.0.0.1', 2911)

ip_packet = "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e"


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server.")

        # message = f"zad13odp;src;{source_port};dst;{destination_port};data;{payload_decoded}"

        # my_socket.send(message.encode())

        # server_answer = my_socket.recv(1024).decode()

        # print(f"Server answer: {server_answer}")

    else:
        print('Connection failed!')

    my_socket.close()
    print("Connection closed on client side.")


if __name__ == '__main__':
    client_program()
