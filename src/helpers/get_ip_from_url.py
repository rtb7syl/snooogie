import helpers.get_top_level_domain
import helpers.get_host_ip


def getIP(url):

    domain = get_top_level_domain.getDomainName(url)

    ip = get_host_ip.getHostIP(domain)

    hostIP = ip['hostIP']

    err = ip['err']

    if (err == None):

        return hostIP

    else:

        print("there's some issue in getting the ip of the domain....")



