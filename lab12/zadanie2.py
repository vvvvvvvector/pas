import socket
import threading
from datetime import datetime

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
        self.write_to_logs(f"Server started on {self.ip}:{self.port}")

        while True:
            client, address = self.sock.accept()

            print(f"Client {address[0]}:{address[1]} connected")
            self.write_to_logs(f"Client {address[0]}:{address[1]} connected")

            threading.Thread(target=self.client_handler,
                             args=(client, address)).start()

    def write_to_logs(self, message):
        with open("logs.txt", "a") as file:
            now = datetime.now()
            timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
            log_entry = f"{timestamp} -> {message}\n"
            file.write(log_entry)

    def client_handler(self, client, address):
        while True:
            try:
                data = client.recv(1024).decode("utf-8")
                if data:
                    print(f"Client {address[0]}:{address[1]} sent: {data}")
                    self.write_to_logs(
                        f"Client {address[0]}:{address[1]} sent: {data}")

                    client.send(data.encode("utf-8"))
                else:
                    self.write_to_logs(
                        f"Client {address[0]}:{address[1]} has disconnected")
                    raise socket.error(
                        f"Client disconnected: {address[0]}:{address[1]}")

            except socket.error as e:
                print(e)
                client.close()
                return False


if __name__ == "__main__":
    Server("127.0.0.1", 2900).listen()
