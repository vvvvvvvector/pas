import socket
import sys

ip_address = sys.argv[1]

hostname = socket.gethostbyaddr(ip_address)

print("Hostname for the {} is: {}".format(ip_address, hostname[0]))
