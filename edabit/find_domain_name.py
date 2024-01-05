import socket

"""
Find Domain Name From DNS Pointer (PTR) Records Using IP Address
"""


def get_domain(ip_address) -> str:
    host_name = socket.gethostbyaddr(ip_address)
    domain_name = host_name[0]

    return domain_name


assert get_domain("8.8.8.8") == "dns.google"
assert get_domain("8.8.4.4") == "dns.google"
