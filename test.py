#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import sys
import sqlite3

cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print
print "python: \n%s\n" % sys.version
print "sqllite: \n%s\n" % sqlite3.version
