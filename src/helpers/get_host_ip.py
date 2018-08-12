import socket

def getHostIP(hostName):

    try:
        hostIP = socket.gethostbyname(hostName)

        return {'hostIP':hostIP,'err':None}

    except socket.error as err:

        return {'hostIP':None,'err':err}

if (__name__ == '__main__'):
    print(getHostIP('google.com'))
    print(getHostIP('dhyamna.io'))

