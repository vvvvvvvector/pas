import socket

host = "127.0.0.1"
port = 2901


def calculate_expression(number_1, operator, number_2):
    print(f"Received expression: {number_1} {operator} {number_2}")

    if operator == "+":
        return float(number_1) + float(number_2)
    elif operator == "-":
        return float(number_1) - float(number_2)
    elif operator == "*":
        return float(number_1) * float(number_2)
    elif operator == "/":
        return float(number_1) / float(number_2)
    else:
        return "Invalid operator"


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))

    print(f"Server started on {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)

        if not data:
            break

        number_1, operator, number_2 = data.decode().split(" ")

        result = calculate_expression(number_1, operator, number_2)

        answer = f"Result: {result}"

        server_socket.sendto(answer.encode(), client_address)

    server_socket.close()

    print("Connection closed on server side")


if __name__ == "__main__":
    server_program()
