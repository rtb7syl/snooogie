from helpers import get_top_level_domain
import whois

def whoisLookup(url):
    
    try:

        domain = get_top_level_domain.getDomainName(url)
        
        whoisData = whois.whois(domain)

    except Exception as e:

        print('whois lookup failed,err : ' + str(e))


        pass

    return whoisData







