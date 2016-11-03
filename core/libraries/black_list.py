import dns.resolver
import dns.exception
import socket

bls = [
    '0spam.fusionzero.com',
    'access.redhawk.org',
    'all.rbl.jp',
    'all.s5h.net',
    'all.spamrats.com',
    'b.barracudacentral.org',
    'bl.blocklist.de',
    'bl.emailbasura.org',
    'bl.mailspike.org',
    'bl.score.senderscore.com',
    'bl.spamcannibal.org',
    'bl.spamcop.net',
    'bl.spameatingmonkey.net',
    'bogons.cymru.com',
    'cblplus.anti-spam.org.cn',
    'cidr.bl.mcafee.com',
    'db.wpbl.info',
    'dnsbl-1.uceprotect.net',
    'dnsbl-2.uceprotect.net',
    'dnsbl-3.uceprotect.net',
    'dnsbl.dronebl.org',
    'dnsbl.inps.de',
    'dnsbl.justspam.org',
    'dnsbl.kempt.net',
    'dnsbl.rv-soft.info',
    'dnsbl.sorbs.net',
    'dnsbl.tornevall.org',
    'dnsbl.webequipped.com',
    'dnsrbl.swinog.ch',
    'fnrbl.fast.net',
    'ips.backscatterer.org',
    'ix.dnsbl.manitu.net',
    'korea.services.net',
    'l2.bbfh.ext.sorbs.net',
    'list.blogspambl.com',
    'mail-abuse.blacklist.jippg.org',
    'psbl.surriel.com',
    'rbl2.triumf.ca',
    'rbl.dns-servicios.com',
    'rbl.efnetrbl.org',
    'rbl.polarcomm.net',
    'spam.abuse.ch',
    'spam.dnsbl.sorbs.net',
    'spam.pedantic.org',
    'spamguard.leadmon.net',
    'spamrbl.imp.ch',
    'spamsources.fabel.dk',
    'st.technovision.dk',
    'tor.dan.me.uk',
    'tor.dnsbl.sectoor.de',
    'truncate.gbudb.net',
    'ubl.unsubscore.com',
    'virbl.dnsbl.bit.nl',
    'zen.spamhaus.org',
    'rbl.megarbl.net',
    'rbl.abuse.ro'
]


def check(domain):
    results = []
    try:
        ip = socket.gethostbyname(domain)
        clear = True
        for bl in bls:
            status = True
            message = ''
            try:
                my_resolver = dns.resolver.Resolver()
                query = '.'.join(reversed(str(ip).split("."))) + "." + bl
                answers = my_resolver.query(query, "A")
                answer_txt = my_resolver.query(query, "TXT")

                message = 'IP: %s IS listed in %s (%s: %s)' % (ip, bl, answers[0], answer_txt[0])
                status = False
                clear = False
            except dns.resolver.NXDOMAIN:
                pass
            except dns.exception.Timeout:
                message = 'Timeout: ' + bl
            except dns.resolver.NoAnswer:
                message = 'NoAnswer: ' + bl
            except dns.resolver.NoNameservers:
                message = 'NoNameServers: ' + bl
            except Exception, exc:
                print type(exc)
                print 'Message: ' + exc.message
                continue

            results.append({
                'status': status,
                'server': bl,
                'message': message
            })

        return clear, results

    except Exception, exc:
        return False, results
