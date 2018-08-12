import tld

def getDomainName(url):
    
    # gets the top-level-domain name for any url,formatted in any way.
    
    try:
        domainName = tld.get_fld(url,fix_protocol=True)
    
    except Exception as e:

        print('Domain name extraction failed. err : ' + e)

        pass

    return domainName



if (__name__ == "__main__"):

    print(getDomainName('https://ww.google.com'))


