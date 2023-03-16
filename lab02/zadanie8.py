import socket
import sys
import ipaddress

server_address = sys.argv[1]

try:
    ipaddress.ip_address(server_address)
except:
    server_address = socket.gethostbyname(server_address)

print(f"Server address: {server_address}")

for port in range(1, 65535):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.settimeout(0.1)

    success_code = my_socket.connect_ex((server_address, port))

    if success_code == 0:
        print(f"Port {port} is open")

        try:
            print(
                f"Name of service running at port {port} : {socket.getservbyport(port, 'tcp')}")
        except OSError:
            print("Service not found")

    my_socket.close()
