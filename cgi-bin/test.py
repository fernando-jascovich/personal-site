#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import sys
import socket

cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print
print socket.gethostbyname(socket.gethostname())
print "python: \n%s\n" % sys.version
