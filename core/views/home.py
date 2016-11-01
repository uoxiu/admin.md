from django.shortcuts import render
from django.conf import settings
from django_user_agents.utils import get_user_agent
from ipware.ip import get_ip
from core.util import validate_ip
import pygeoip
import socket


def index(request):
    geo_ip_country = pygeoip.GeoIP(settings.GEOIP_COUNTRY_PATH)
    geo_ip_isp = pygeoip.GeoIP(settings.GEOIP_ISP_PATH)

    my_ip = get_ip(request)

    ip = request.GET.get('ip', my_ip)

    if not validate_ip(ip):
        try:
            ip = socket.gethostbyname(ip)
        except:
            ip = my_ip

    context = {
        'ip': ip,
        'addr': {
            'country': geo_ip_country.country_name_by_addr(ip),
            'isp': geo_ip_isp.isp_by_addr(ip),
            'hostname': socket.gethostbyaddr(ip)[0]
        },
        'user_agent': get_user_agent(request),
        'language': request.LANGUAGE_CODE
    }

    return render(request, 'pages/home.html', context)
