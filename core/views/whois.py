from django.shortcuts import render
from django.http import JsonResponse
from core.util import reverse_dns, validate_domain
import pythonwhois


def index(request):
    domain = request.GET.get('domain', '')

    is_valid = validate_domain(domain)

    context = {
        'domain_valid': is_valid,
        'domain': domain,
    }

    return render(request, 'pages/whois.html', context)


def get_info(request):
    domain = request.GET.get('domain', '')
    is_valid = validate_domain(domain)

    if is_valid:

        try:
            whois_info = pythonwhois.get_whois(domain)
        except:
            whois_info = {}

        if whois_info:
            return JsonResponse({
                'error': 0,
                'message': ''.join(whois_info['raw']) if whois_info['raw'] else 'No whois info'
            })
        else:
            return JsonResponse({
                'error': 1,
                'message': 'No whois info'
            })

    else:
        return JsonResponse({
            'error': 1,
            'message': 'Invalid domain'
        })
