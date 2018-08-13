# snooogie

## A proof-of-concept, minimal, multi-threaded , concurrent , TCP Connect port scanner and reconnaissance tool , which can scan and gather info about single/multiple host/s concurrently


 It serves as a port scanner,where it scans for any range of TCP ports of any host ,and identifies them as either open or closed.
 It also gives info about different whois queries .


 It takes different inputs as command-line arguments,and spits out a huugeee pretty-printed object of different info
 about host(s) and its/their range of ports to scan.


 As,of now it supports only 3 different kinds (sets) of command line args,each of them serving quite a different purpose


* Takes in a JSON file path(absolute),containing info (url/domain name, range of ports to be scanned) about various hosts,
  and number of processes to be spawned for concurrent scanning of multiple hosts,and logs a pretty-printed JSON object containing
  info of all those hosts. cd
     
   > The JSON file has the following format : 
     
     
       ['{"hostURL : <host_url0>,"minPort":<min_port0>,"maxPort":<max_port0>}',
        '{"hostURL : <host_url1>,"minPort":<min_port1>,"maxPort":<max_port1>}' ,
        '{"hostURL : <host_url2>,"minPort":<min_port2>,"maxPort":<max_port2>}' ,
         .............
         .............
       ]

    For this just clone the project.
    
    ```
    $ git clone https://github.com/rtb7syl/snooogie.git
    $ cd src
    $ python main.py -j <abs path of JSON file> -n <no. of processes to be spawned>
    
    ```
    > The output JSON has the following fields:
      
      [
       {
        'address': ,
        'city': ,
        'closedPorts': [],
        'country': ,
        'creation_date': [],
                          
        'dnssec': ,
        'domain_name': [],
        'emails': [],
        'expiration_date': [],
        
        'hostIP': ,
        'name': ,
        'name_servers': []
                         
        'openPorts': [],
        'org': ,
        'referral_url': ,
        'registrar': ,
        'state': ,
        'status': [],
        'updated_date': [],
        'whois_server': ,
        'zipcode': 
        
        },
        
        ........
        ........
        ........
        
      ]
      
      
      
* Takes in a host IP , min-port and max-port as arguments ,and spits out a pretty-printed JSON containing all the recon info.

   ```
   $ git clone https://github.com/rtb7syl/snooogie.git
   $ cd src
   $ python main.py -hIP <IP of host> -minP <min port> -maxP <max port>
   
   ```
   
   > The output JSON has the following fields :
   
        {
        'address': ,
        'city': ,
        'closedPorts': [],
        'country': ,
        'creation_date': [],
                          
        'dnssec': ,
        'domain_name': [],
        'emails': [],
        'expiration_date': [],
        
        'hostIP': ,
        'name': ,
        'name_servers': []
                         
        'openPorts': [],
        'org': ,
        'referral_url': ,
        'registrar': ,
        'state': ,
        'status': [],
        'updated_date': [],
        'whois_server': ,
        'zipcode': 
        
        }





* Takes in a host domain name/url , min-port and max-port as arguments ,and spits out a pretty-printed JSON containing all the recon info.

   ```
   $ git clone https://github.com/rtb7syl/snooogie.git
   $ cd src
   $ python main.py -u <host domain name or url> -minP <min port> -maxP <max port>
   
   ```
   
   > The output JSON has the following fields :
   
        {
        'address': ,
        'city': ,
        'closedPorts': [],
        'country': ,
        'creation_date': [],
                          
        'dnssec': ,
        'domain_name': [],
        'emails': [],
        'expiration_date': [],
        
        'hostIP': ,
        'name': ,
        'name_servers': []
                         
        'openPorts': [],
        'org': ,
        'referral_url': ,
        'registrar': ,
        'state': ,
        'status': [],
        'updated_date': [],
        'whois_server': ,
        'zipcode': 
        
        }

Use the --help flag if you run into any trouble.

```
$ python main.py -h

```

Also if you want some service to communicate with this app, it's kinda easy too. Cause communication happens through an easy to parse JSON object.

Just clone the project, view the main.py file ( the entry point of this project ).
Import the module ,and use which-ever utility you need.

Also there's some helper utility modules under src/helpers, which provides some basic utility functions like getting top-level domain names, getting ip from a domain-name etc.

Use them as,you wish. 

The code is quite modular, there's also quite a bit documentation in form of comments in between codes too :P 
It'd be not too hard to use them, or customize them according to your own needs,if you wish.


The project is not yet complete,and under development.

Future avenues I want to explore:

* TCP ACK / SYN scans to speed my scanner more , and also to determine whether the port is actually closed or a firewall rule is            blocking the incoming packets.

*  TCP FIN scan

*  UDP scan

*  Use multiprocessing to spawn mutiple child processes to batch scan multiple ports concurrently, so that TCP connect scan becomes  faster

