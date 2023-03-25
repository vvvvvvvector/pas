import socket

server_address = ('127.0.0.1', 2911)

ip_packet = "4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e"


def client_program():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.settimeout(1.0)

    success = my_socket.connect_ex(server_address)

    if success == 0:
        print("Successfully connected to the server.")

        protocol_version = int(ip_packet[0:1], 16)

        print(f"Protocol version: {protocol_version}")

        protocol_type = int(ip_packet[18:20], 16)

        print(f"Protocol type: {protocol_type}")

        source_ip = ip_packet[24:32]
        sourse_ip_str = f"{int(source_ip[0:2], 16)}.{int(source_ip[2:4], 16)}.{int(source_ip[4:6], 16)}.{int(source_ip[6:8], 16)}"

        print(f"Source IP: {sourse_ip_str}")

        destination_ip = ip_packet[32:40]
        destination_ip_str = f"{int(destination_ip[0:2], 16)}.{int(destination_ip[2:4], 16)}.{int(destination_ip[4:6], 16)}.{int(destination_ip[6:8], 16)}"

        print(f"Destination IP: {destination_ip_str}")

        message = f"zad15odpA;ver;{protocol_version};srcip;{sourse_ip_str};dstip;{destination_ip_str};type;{protocol_type}"

        my_socket.send(message.encode())

        server_answer = my_socket.recv(1024).decode()

        print(f"Server answer: {server_answer}")

        if server_answer == "TAK":
            source_port = int(ip_packet[40:44], 16)
            destinatain_port = int(ip_packet[44:48], 16)

            payload = ip_packet[104:]
            payload_bytes = bytes.fromhex(payload)
            payload_decoded = payload_bytes.decode()

            print(f"Source port: {source_port}")
            print(f"Destination port: {destinatain_port}")
            print(f"Payload: {payload_decoded}")

            another_message = f"zad15odpB;srcport;{source_port};dstport;{destinatain_port};data;{payload_decoded}"

            my_socket.send(another_message.encode())

            another_server_answer = my_socket.recv(1024).decode()

            print(f"Server answer: {another_server_answer}")

    else:
        print('Connection failed!')

    my_socket.close()
    print("Connection closed on client side.")


if __name__ == '__main__':
    client_program()
