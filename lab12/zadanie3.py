import socket
import threading
import random
import numbers

# python ../lab02/zadanie3.py -> example client program


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))

    def listen(self):
        self.sock.listen(5)

        print(f"Server started on {self.ip}:{self.port}")

        while True:
            client, address = self.sock.accept()

            print(f"Client {address[0]}:{address[1]} connected")

            client.settimeout(60)

            threading.Thread(target=self.client_handler,
                             args=(client, address)).start()

    def client_handler(self, client, address):
        server_random = random.randint(1, 50)

        print(
            f"Server random number = {server_random} for {address[0]}:{address[1]} client")

        while True:
            try:
                data = client.recv(1024)

                if not data:
                    print(
                        f"Connection {address[0]}:{address[1]} was closed on client side")
                    break

                client_number = None

                try:
                    client_number = int(data.decode('utf-8'))

                except ValueError:
                    client.send(
                        f"{data.decode()} -> is not an integer!".encode())

                    print(f"{data.decode()} -> is not an integer!")

                if isinstance(client_number, numbers.Integral):
                    server_answer = ""

                    if client_number == server_random:
                        server_answer = "You win!"
                    elif client_number > server_random:
                        server_answer = "Too much!"
                    else:
                        server_answer = "Too little!"

                    client.send(server_answer.encode())

            except socket.error as e:
                print(e)
                client.close()
                return False


if __name__ == "__main__":
    Server("127.0.0.1", 2900).listen()
