from socket import *
from queue import Queue
from helpers.whois_lookup import *

import threading,time

def scanHost(hostIP,port,connCode=1):

    #function which takes in the host IP addr and port number of a host
    #and checks whether that port is open or not

    #function returns a dict containing info about port status code (open/closed)
    #and err/exception info

    addr = (hostIP,port)
    err = None

    try:

        sock = socket(AF_INET,SOCK_STREAM)

        code = sock.connect_ex(addr)

        if (code == 0):

            connCode = code
        
        sock.close()

    except Exception as e:

        err = e

        pass
    

    #connCode is  0 if port is open,and 1 otherwise
    #err is None if there's no exception ,and otherwise,e if any exception occurs


    return {'connCode':connCode,'err':err}






def isPortOpen(scanResult):

    #function takes in the scan result dict,ie the return value of scanHost(args)
    #returns True if port is open,False otherwise

    connCode = scanResult['connCode']

    portStatus = True if (connCode == 0) else False

    return portStatus





def logScanResult(hostIP,port,scanResult):
    
    #logs the port scan result
    #print('*'*10)

    portStatus = isPortOpen(scanResult)

    err = scanResult['err']




    portLiveStatusLog = 'Host IP: '+hostIP+' Port No. ' + str(port) + ' is open' if (portStatus) else 'Host IP : '+hostIP+' Port No. ' +str(port) + ' is closed'
    




    if (err != None):

        #if there's some error/exception while scanning the port,just log the error

        print('There seems to be some error : ',err)

    else:
        
        #else,just log the port status
        
        print(portLiveStatusLog)






#There can be any of these two types of main jobs. We're using the
#second one as of now,cause it returns open/closed ports in a nice #structural way,not just logs port statuses in a dumb fashion.


#job subroutine type 1
def scanHostAndLogResultJob(hostIP,port):

    #main job
    #takes in host IP and port,scans the port and logs the result
    
    scanResult = scanHost(hostIP,port)

    logScanResult(hostIP,port,scanResult)





#job subroutine type 2
def scanHostAndEnqueueJob(hostIP,port):

    #main job
    #scans ports and enqueues open and closed ports
    #in their correspondng queues
    

    scanResult = scanHost(hostIP,port)

    err = scanResult['err']
    portStatus = isPortOpen(scanResult)


    if (err == None):
        #if no error

        if (portStatus):
            #if open port

            openPortsQueue.put(port)

        else:
            #if closed port

            closedPortsQueue.put(port)



def threader(hostIP,lock):
   
    # threader pulls a task (port) from the queue,and
    #sends it to scanHostAndLogResultJob(args) subroutine to process it



    while True:

        #gets a task (port) from queue
        port = taskQueue.get()
        
        with lock:

            print('Wait...................!!')
        

        #sends it to this subroutine job to process it
        #scanHostAndEnqueueJob(hostIP,port)

        scanHostAndEnqueueJob(hostIP,port)
        
        with lock:
            
            # locking print,so that only one thread logs to console at a time

            print("Just a li'l bit more,I promise ya.....")



        #done with the job,all tasks processed,queue empty,
        #informs task queue.join() to release the main thread

        taskQueue.task_done()




def main(hostIP,minPort,maxPort,lock):
    
    #main entry point of the program
    #returns a dictionary of open and closed ports b/w the
    #range of ports provided
    

    

    #spawns 35 threads(workers)
    for i in range(35):

        worker = threading.Thread(target = threader,args = (hostIP,lock),daemon = True)
        
        worker.start()


    
    #assigns tasks,ie enqueues the task queue with the ports to be scanned
    for port in range(minPort,maxPort + 1):

        taskQueue.put(port)

    
    #release the main thread when queue is empty,ie all processing done
    taskQueue.join()

    #all threads killed,main thread processing resumes,hereafter



    #open and closed ports lists
    openPorts = list(openPortsQueue.queue)
    closedPorts = list(closedPortsQueue.queue)



    #scan data dictionary to be returned    
    portScanData = {'hostIP':hostIP,'closedPorts':closedPorts,'openPorts':openPorts}
    
    
    return portScanData






#create task queue
taskQueue = Queue()


closedPortsQueue = Queue()
openPortsQueue = Queue()


lock = threading.Lock()

if (__name__ == "__main__"):



    hostIP = '34.227.231.8'
    minPort,maxPort = (25,30)


    
    
    print(main(hostIP,minPort,maxPort,lock))











