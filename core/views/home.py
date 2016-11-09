from django.shortcuts import render
from django.conf import settings
from django_user_agents.utils import get_user_agent
from ipware.ip import get_ip
from core.util import prepare_ip
from core.util import reverse_dns
import pygeoip

def index(request):
    geo_ip_country = pygeoip.GeoIP(settings.GEOIP_COUNTRY_PATH)
    geo_ip_isp = pygeoip.GeoIP(settings.GEOIP_ISP_PATH)

    input_address = request.GET.get('ip', None)

    if input_address is None:
        ip = get_ip(request)
    else:
        ip = prepare_ip(input_address)

    if ip:
        address = {
            'ip': ip,
            'country': geo_ip_country.country_name_by_addr(ip),
            'isp': geo_ip_isp.isp_by_addr(ip),
            'hostname': reverse_dns(ip),
        }
    else:
        address = {}

    context = {
        'input_address': input_address,
        'address': address,
        'user_agent': get_user_agent(request),
        'language': request.LANGUAGE_CODE
    }

    return render(request, 'pages/home.html', context)
