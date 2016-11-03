from django.shortcuts import render
from django.http import JsonResponse
from django.template import loader
from core.util import prepare_ip
from core.libraries import black_list

def index(request):
    ip = request.GET.get('ip', '')
    ip = prepare_ip(ip)

    context = {
        'ip': ip if ip else ''
    }

    return render(request, 'pages/black-list.html', context)


def check(request):
    ip = request.GET.get('ip', '')
    ip = prepare_ip(ip)

    if ip:

        status, results = black_list.check(ip)

        context = {
            'status': status,
            'results': results
        }

        return JsonResponse({
            'error': 1,
            'message': loader.render_to_string('pages/black-list-result.html', context, request)
        })

    else:
        return JsonResponse({
            'error': 1,
            'message': 'Invalid IP'
        })
