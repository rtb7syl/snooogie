# snooogie
## A multi-threaded ,concurrent,TCP Connect port scanner and reconnaissance tool , which can scan and gather info about single/multiple host/s concurrently


 It serves as a port scanner,where it scans for any range of TCP ports of any host ,and identifies them as their open or closed.
 It also gives info about different whois queries .


 It takes different inputs as command-line arguments,and spits out a huugeee pretty-printed object of different info
 about host(s) and its/their range of ports to scan.


 As,of now it supports only 3 different kinds (sets) of command line args,each of them serving quite a different purpose

 *  Takes in a JSON file path(absolute),containing info (url/domain name, range of ports to be scanned) about various hosts,
     and number of processes to be spawned for concurrent scanning of multiple hosts,and logs a pretty-printed JSON object containing
     info of all those hosts. 
     
   > The JSON file has the following format : 
     
     
       ['{"hostURL : <host_url0>,"minPort":<min_port0>,"maxPort":<max_port0>}',
        '{"hostURL : <host_url1>,"minPort":<min_port1>,"maxPort":<max_port1>}' ,
        '{"hostURL : <host_url2>,"minPort":<min_port2>,"maxPort":<max_port2>}' ,
         .............
         .............
       ]

     
