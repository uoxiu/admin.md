import re
import requests


def find_domains(content):
    domains = []

    results = re.findall(r"\<cite\>([\w\.0-9\/]+)\<\/cite\>", content)

    for result in results:
        domains.append(result.split('/')[0])

    return domains


def domains(ip):
    url = 'http://' + 'ww' + 'w.bi' + 'ng.' + 'com/se' + 'arch?' + 'q=ip:' + ip
    response = requests.get(url, timeout=1)
    pages = re.findall(r"aria-label=\"\w+ \d+\" href=\"([^\"]+)\"", response.content)
    domains = find_domains(response.content)
    for page in list(set(pages)):
        response = requests.get('http://w' + 'ww.b' + 'ing' + '.com' + page)
        domains += find_domains(response.content)

    return list(set(domains))
