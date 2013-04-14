#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

try:
    import json
except ImportError:
    import simplejson as json

import model.util

print 'Content-type: text/html'
print

'''
class BasePage:
    def __init__(self):
        self.name = 'base'
        self.pages = {
        "home": "",
        "abstract": "",
        "geek": "",
        "contact": ""
        }
'''
#model.util.createDataModel(BasePage())

#data = model.util.getDataModel('base')

#print data["home"]
print 'fer'
print "\n"
