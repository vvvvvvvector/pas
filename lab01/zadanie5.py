import socket
import sys

hostname = sys.argv[1]

ip_address = socket.gethostbyname(hostname)

print("IP address of the {} is: {}".format(hostname, ip_address))
