import socket

server_address = ('127.0.0.1', 2910)

udp_datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server.")

        source_port = int(udp_datagram[0:4], 16)
        destination_port = int(udp_datagram[4:8], 16)
        length = int(udp_datagram[8:12], 16)
        checksum = int(udp_datagram[12:16], 16)

        payload_hex = udp_datagram[16:]
        payload_bytes = bytes.fromhex(payload_hex)

        payload_decoded = payload_bytes.decode()

        print(f"Source port: {source_port}")
        print(f"Destination port: {destination_port}")
        print(f"Length: {length}")
        print(f"Checksum: {checksum}")
        print(f"Data: {payload_decoded}")

        message = f"zad14odp;src;{source_port};dst;{destination_port};data;{payload_decoded}"

        my_socket.send(message.encode())

        server_answer = my_socket.recv(1024).decode()

        print(f"Server answer: {server_answer}")

    else:
        print('Connection failed')

    my_socket.close()
    print("Connection closed on client side.")


if __name__ == '__main__':
    client_program()
