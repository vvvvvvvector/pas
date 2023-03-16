import socket
import sys
import ipaddress

server_address = sys.argv[1]
server_port = int(sys.argv[2])

try:
    ipaddress.ip_address(server_address)
except:
    server_address = socket.gethostbyname(server_address)

print("Server address: {}, Server port {}".format(server_address, server_port))

try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.settimeout(1.0)

    my_socket.connect((server_address, server_port))

    print("Connected to server: ", server_address, ":", server_port)

    try:
        print(
            f"Name of service running at port {server_port} : {socket.getservbyport(server_port, 'tcp')}")
    except OSError:
        print("Service not found")

    my_socket.close()

except socket.error as msg:
    print("Error: ", msg)
    sys.exit(1)
