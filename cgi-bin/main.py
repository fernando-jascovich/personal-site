#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

import model.util
import view.head

print 'Content-type: text/html'
print

page = model.util.BasePage('no-token')
data = model.util.getDataModel(page)

print view.head.getHead('js')
print '<html>'
print data
print '</html>'
