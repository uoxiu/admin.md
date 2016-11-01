from django.shortcuts import render
from django.http import JsonResponse
from core.util import validate_ip
from core.libraries import bing
import socket


def index(request):
    ip = request.GET.get('ip', '')
    if ip and not validate_ip(ip):
        try:
            ip = socket.gethostbyname(ip)
        except:
            ip = ''

    context = {
        'ip': ip
    }

    return render(request, 'pages/reverse-ip.html', context)


def find_domains(request):
    ip = request.GET.get('ip', '')

    if ip and validate_ip(ip):

        domains = bing.domains(ip)

        if domains:
            return JsonResponse({
                'error': 0,
                'list': domains
            })
        else:
            return JsonResponse({
                'error': 1,
                'message': 'Domains not found'
            })

    else:
        return JsonResponse({
            'error': 1,
            'message': 'Invalid IP'
        })
