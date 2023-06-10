import socket
import threading
import ssl
from OpenSSL import crypto


def generate_cert():
    cert = crypto.X509()

    cert.get_subject().C = "PL"
    cert.get_subject().ST = "Lubelskie"
    cert.get_subject().L = "Lublin"
    cert.get_subject().O = "UMCS"
    cert.get_subject().OU = "PAS"
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(0)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.set_issuer(cert.get_subject())

    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 4096)

    cert.set_pubkey(key)
    cert.sign(key, "sha512")

    cert_file = "server.crt"
    key_file = "server.key"

    with open(cert_file, "wt") as f:
        f.write(crypto.dump_certificate(
            crypto.FILETYPE_PEM, cert).decode())
    with open(key_file, "wt") as f:
        f.write(crypto.dump_privatekey(
            crypto.FILETYPE_PEM, key).decode())

    return cert_file, key_file


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))

    def listen(self):
        self.sock.listen(10)

        print(f"Server started on {self.ip}:{self.port}")

        while True:
            client, address = self.sock.accept()

            print(f"Client {address[0]}:{address[1]} connected")

            client.settimeout(60)

            threading.Thread(target=self.client_handler,
                             args=(client, address)).start()

    def client_handler(self, client, address):
        while True:
            try:
                data = client.recv(1024).decode("utf-8")
                if data:
                    print(f"Client {address[0]}:{address[1]} sent: {data}")
                    client.send(data.encode("utf-8"))
                else:
                    raise socket.error("Client disconnected")
            except socket.error as e:
                print(e)
                client.close()
                return False


if __name__ == "__main__":
    cert_file, key_file = generate_cert()

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)

    server = Server("127.0.0.1", 2900)

    with context.wrap_socket(server.sock, server_side=True) as ssl_socket:
        server.sock = ssl_socket
        server.listen()
