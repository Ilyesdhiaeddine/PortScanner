#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid amount of argument ")
    print("Syntax: python3 port_scanner.py <ip>")

print(".-" * 80)
print("Scanning target " + target)
print("Time started " + str(datetime.now()))
print("-." * 80)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.01)
        result = s.connect_ex((target,port))
        # print("Checking port " + str(port))
        if result == 0:
            print(str(port) + " is open")
        s.close()
except KeyboardInterrupt:
    print("Exiting Program")
    sys.exit()
except socket.gaierror:
    print("host name could not be resolved")
    sys.exit()
except socket.error:
    print("could not connect to server")
    sys.exit()
