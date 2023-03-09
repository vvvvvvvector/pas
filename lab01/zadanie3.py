import ipaddress

print("Write the IP address to validate:")
ip_string = input()


def validate_ip_address(ip):
    try:
        result = ipaddress.ip_address(ip)
        print("The IP address {} is valid".format(result))
    except ValueError:
        print("The IP address is not valid!")


validate_ip_address(ip_string)
