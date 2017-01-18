import socket
import re

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def prepare_ip(ip):
    if ip and not validate_ip(ip):
        try:
            ip = socket.gethostbyname(ip)
        except:
            ip = None

    return ip if ip else None


def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return ''


def validate_domain(value):
    if value:
        if not re.match(
                r"^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\.[a-zA-Z]{2,3})$",
                value, re.IGNORECASE):
            return False

        return True

    return False