#Created 11/08/2018,4:24 AM IST
#Author: Ritabrata Sanyal/rtb7syl


#Lightweight,multi-threaded ,concurrent TCP Connect Port Scanner

#Mainly operates in these two following ways:

# > Reads a JSON file containing data about multiple hosts,that being,
#  url of host and range of ports to be scanned
#  spits out a large JSON containg IP of those hosts,domain names of them,
#  and two arrays containing info about which ports are open ,or closed
#  for each host in input JSON



# > Takes in a host url,and range of ports to be scanned, as input from user
#   and spits out a json containg all those info as above



#Multi-threaded and concurrent ( ie any number of child  processes can be
# spawned by user,so that a large  number of hosts can be scannned concurrently)  






from scan import scan_many as smh

import scan.scan_one as sco
import sys
import json
import re
from helpers import get_ip_from_url

from pprint import pprint

from helpers.whois_lookup import *

import argparse










def check_args(args=None):
        
        
    parser = argparse.ArgumentParser(description='TCP Connect Scan of single/multiple hosts/host for a range of ports')
    
    parser.add_argument('-hIP', '--hostIP',help='host ip')
    
    parser.add_argument('-minP', '--minPort',help='min port to be scanned')

    parser.add_argument('-maxP', '--maxPort',help='max port to be scanned')
    
    parser.add_argument('-j', '--jsonFilePath',help='hosts data json file')
    
    parser.add_argument('-n', '--nProcesses',help='number of processes to be spawned for processing  multiple hosts data concurrently')
    
    parser.add_argument('-u', '--url',help='url or hostname to be scanned')
    results = parser.parse_args(args)



    resultsDict = {'hostIP':results.hostIP,'hostName':results.url,'minPort':results.minPort,'maxPort':results.maxPort,'jsonFilePath':results.jsonFilePath,'n_procs':results.nProcesses}
    
    return resultsDict





def helper1(jsonFilePath,n_procs):

    #takes a json file containing data about multiple hosts,
    #and number of  processes to be spawned to scan them concurrently
    #pretty prints the scan result


        with open(jsonFilePath) as jsonFile:

            hostsData = json.loads(jsonFile)
            

        print(' Hosts Data : ')
        pprint(hostsData)


        hostsScanData = smh.completeJobs(hostsData,smh.urlQueue,smh.hostsScanResultsQueue,smh.lock,n_procs=n_procs)
        

        pprint(hostsScanData)








def helper2(hostIP,minPort,maxPort):

    #scans a single host IP,for a range of ports as provided.

    ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";

    hostRaw = re.compile(ValidIpAddressRegex)
    
    checkMatch = hostRaw.match(hostIP)


    if (checkMatch != None):

        #valid IP

        print(sco.main(hostIP,minPort,maxPort,sco.lock))


    else:

        print('Invalid IP,mate')



def helper3(hostName,minPort,maxPort):

    #scans a single hostname,for a range of ports as provided
    

    whoisLookupData = whoisLookup(hostName)



    hostIP = get_ip_from_url.getIP(hostName)
    portScanData = sco.main(hostIP,minPort,maxPort,sco.lock)

    

    for key in  whoisLookupData:

        portScanData[key] = whoisLookupData[key]







    print(portScanData)







    










    

def  main():
    
    #main entry point

    
    args = sys.argv[1:]
    
    validArgs1 = ['jsonFilePath','n_procs']

    validArgs2 = ['hostIP','minPort','maxPort']
    
    validArgs3 = ['hostName','minPort','maxPort']

    argResults = check_args(args)
    
    argsSupplied = []
    argsVal = []


    for arg in argResults:
        
        argVal = argResults[arg]

        if (argVal != None):

            argsSupplied.append(arg)

            argsVal.append(argVal)


    print(argsSupplied)
    print(argsVal)


    if (set(validArgs1) == set(argsSupplied)):

        jsonFilePath,n_procs = argsVal
    
        helper1(jsonFilePath,int(n_procs))

    elif (set(validArgs2) == set(argsSupplied)):

        hostIP,minPort,maxPort = argsVal

        helper2(hostIP,int(minPort),int(maxPort))



    elif (set(validArgs3) == set(argsSupplied)):

        hostName,minPort,maxPort = argsVal
        
        
        
        helper3(hostName,int(minPort),int(maxPort))


    else:

        print('DUDE....refer the --help,and enter the proper arguments already!!!')


    
    print('All done.....Adios')    
    


main()




