import socket

server_address = ('127.0.0.1', 2909)

tcp_segment = "0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29"


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server.")

        source_port = int(tcp_segment[0:4], 16)  # 16 bits - 4 symbols
        destination_port = int(tcp_segment[4:8], 16)  # 16 bits - 4 symbols

        # sequence_number = ... 32 bits - 8 symbols
        # acknowledgement_number = ... 32 bits - 8 symbols
        # this_thing = ... 16 bits - 4 symbols
        # window = ... 16 bits - 4 symbols
        # checksum = ... 16 bits - 4 symbols
        # urgent_pointer = ... 16 bits - 4 symbols
        # options = ... 12 bytes -> 96 bits - 24 symbols
        # payload = ... 4 + 4 + 8 + 8 + 4 + 4 + 4 + 4 + 24 -> from 64th symbol

        print(f"Source port: {source_port}")
        print(f"Destination port: {destination_port}")

        payload_hex = tcp_segment[64:]
        payload_bytes = bytes.fromhex(payload_hex)
        payload_decoded = payload_bytes.decode()

        print(f"Payload: {payload_decoded}")

        message = f"zad13odp;src;{source_port};dst;{destination_port};data;{payload_decoded}"

        my_socket.send(message.encode())

        server_answer = my_socket.recv(1024).decode()

        print(f"Server answer: {server_answer}")

    else:
        print('Connection failed!')

    my_socket.close()
    print("Connection closed on client side.")


if __name__ == '__main__':
    client_program()
