from django.shortcuts import render
from django.http import JsonResponse
from core.util import prepare_ip
from core.libraries import bing
from core.util import reverse_dns
import socket


def index(request):
    ip = request.GET.get('ip', '')
    ip = prepare_ip(ip)

    context = {
        'ip': ip if ip else ''
    }

    return render(request, 'pages/reverse-ip.html', context)


def find_domains(request):
    ip = request.GET.get('ip', '')
    ip = prepare_ip(ip)

    if ip:

        domains = bing.domains(ip)

        reverse_domain = reverse_dns(ip)
        if reverse_domain:
            domains.append(reverse_domain)

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
