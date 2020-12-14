#!/usr/bin/python
# This script contains code that was adapted from pythonforbeginners.com "Port Scanner in Python" by unspecified author, this script also contains code that was reviewed during the lecture on 9/8
# This script will perform a port scan of an input ip  from ports 1-1024 when executed
# Name: Sofia Martinez, ITMS-543

import socket
import time
sTime = time.time()

# ask user to input an ip address
ip = raw_input("Enter an IP  to scan: ")
print " "
print "Scanning IP.......", ip
print " "
print "Scan Results:"

# for loop to test ports 1 - 1024
for p in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((ip, p))
    if status == 0:
        print "Port", p, "is open"
    s.close()

# determine total time taken and print result
tTime = round(time.time() - sTime)
print " "
print "Total run time.......", tTime, "seconds"
