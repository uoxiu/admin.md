import socket

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