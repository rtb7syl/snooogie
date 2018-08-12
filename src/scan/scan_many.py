import multiprocessing
import scan.scan_one as sco

from helpers import get_top_level_domain
from helpers import get_host_ip

from queue import Queue

from helpers.whois_lookup import *

def job(hostURL,minPort,maxPort,hostsScanResultsQueue,lock):

    domain = get_top_level_domain.getDomainName(hostURL)
    
    whoisLookupData = whoisLookup(domain)

    
    ipInfo = get_host_ip.getHostIP(domain)
   
    hostIP = ipInfo['hostIP']

    err = ipInfo['err']


    if (err == None):
        
        hostScanData = {'url':hostURL,'domainName':domain,'hostIP':hostIP}

       
        portScanData = sco.main(hostIP,minPort,maxPort,sco.lock)
        
        hostScanData['openPorts'] = portScanData['openPorts']
        hostScanData['closedPorts'] = portScanData['closedPorts']
        

        for key in whoisLookupData:

            hostScanData[key] = whoisLookupData[key]


        hostsScanResultsQueue.put(hostScanData)



    else:

        lock.acquire()
        print('Failed to resolve host IP from domain name,err : '+ err)
        lock.release()




def worker(urlQueue,hostsScanResultsQueue,lock):


    for url in iter( urlQueue.get, None ):

        #url = urlQueue.get()
        
        hostURL = url['hostURL']
        minPort = url['minPort']
        maxPort = url['maxPort']

        job(hostURL,minPort,maxPort,hostsScanResultsQueue,lock)
        
        urlQueue.task_done()

    urlQueue.task_done()





def completeJobs(urls,urlQueue,hostsScanResultsQueue,lock,n_procs=5):
    
    #takes in an array of urls
    procs = []

    # distributing all the tasks among n processes
    for i in range(n_procs):
       

        p = multiprocessing.Process(target=worker,args=(urlQueue,hostsScanResultsQueue,lock),daemon=True)

        procs.append(p)

        p.start()




    for url in urls:

        urlQueue.put(url)

   
    urlQueue.join()

    for p in procs:
        urlQueue.put( None )

    urlQueue.join()

    for p in procs:
        p.join()
    
    hostsScanResultsArray = []

    while not hostsScanResultsQueue.empty():

        hostsScanResultsArray.append(hostsScanResultsQueue.get())

    
    return hostsScanResultsArray

    print("Finished all jobs....")
    print("num active children:", multiprocessing.active_children())






urlQueue = multiprocessing.JoinableQueue()

hostsScanResultsQueue = multiprocessing.Queue()

lock = multiprocessing.Lock()


if (__name__ == '__main__'):

    urls = [{'hostURL':'www.google.com','minPort':25,'maxPort':80},{'hostURL':'www.facebook.com','minPort':25,'maxPort':100},{'hostURL':'www.pornhub.com','minPort':40000,'maxPort':40050},{'hostURL':'www.4chan.com','minPort':200,'maxPort':220},{'hostURL':'www.stripchat.com','minPort':500,'maxPort':530},{'hostURL':'www.yahoo.com','minPort':25,'maxPort':31}]

    
    
    print(completeJobs(urls,urlQueue,hostsScanResultsQueue,lock,n_procs=10))


    print('finished all jobs....exiting')

        


