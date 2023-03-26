import socket

host = "127.0.0.1"
port = 2909


def check_answer(data_decoded):
    data_array = data_decoded.split(";")

    try:
        if data_array[2] == "2900" and data_array[4] == "35211" and data_array[6] == "hello :)":
            return "TAK"
        else:
            return "NIE"

    except IndexError:
        return "BAD SYNTAX"


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))

    print(f"Server started on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)

        if not data:
            break

        result = check_answer(data.decode())

        server_socket.sendto(result.encode(), client_address)

    server_socket.close()

    print("Connection closed on server side")


if __name__ == "__main__":
    server_program()
