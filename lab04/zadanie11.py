import socket

host = "127.0.0.1"
port = 2911


def check_answer_B(data_decoded):
    data_array = data_decoded.split(";")

    try:
        if int(data_array[2]) == 2900 and int(data_array[4]) == 47526 and data_array[6] == "network programming is fun":
            return "TAK"
        else:
            return "NIE"

    except IndexError:
        return "BAD SYNTAX"


def check_answer_A(data_decoded):
    data_array = data_decoded.split(";")

    try:
        if int(data_array[2]) == 4 and data_array[4] == "212.182.24.27" and data_array[6] == "192.168.0.2" and int(data_array[8]) == 6:
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

        data_decoded = data.decode()

        if data_decoded.startswith("zad15odpA"):
            result = check_answer_A(data_decoded)

            server_socket.sendto(result.encode(), client_address)

        elif data_decoded.startswith("zad15odpB"):
            result = check_answer_B(data_decoded)

            server_socket.sendto(result.encode(), client_address)

        else:
            server_socket.sendto("BAD SYNTAX".encode(), client_address)

    server_socket.close()

    print("Connection closed on server side")


if __name__ == "__main__":
    server_program()
