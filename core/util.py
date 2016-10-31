def is_tor(ip):
    import urllib

    tor = urllib.urlopen('https://check.torproject.org/exit-addresses')

    for ip_tor in tor.readlines():
        ip_tor = ip_tor.replace("\n", "")
        if "ExitAddress" in ip_tor:
            ip_tor = ip_tor.split(" ")[1]
            if ip == ip_tor:
                return True

    return False
