#name IP Counter
#author Harijith R
#company VIPoint Solutions
#version  1.0.6

import collections
import sys
import os

LogFile = "/home/harijith/Python/access.log"

# This will exclude the Loopback IP Address both in IPV4 and IPV6
EXCLUDES = ('127.0.0.1','::1')

ipCounter = collections.Counter()

with open(LogFile,'r') as fobj:
  for logLine in fobj:
    ip = logLine.split()[0]
    if ip not in EXCLUDES:
      ipCounter.update((ip,))
      
#print(ipCounter.most_common(5))
#print()
#print('-' * 25)
#print(ipCounter.most_common(5)[::-1])

for ip,count in ipCounter.most_common(5):
  print('{:15}  : {}'.format(ip,count))
