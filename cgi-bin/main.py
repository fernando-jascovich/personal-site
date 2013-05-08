#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

import model.util
import view.head
import view.body


print 'Content-type: text/html'
print

page = model.util.BasePage('no-token')
data = model.util.getDataModel(page)
title = model.util.getXMLData(data['Home'], 'title')
tag = model.util.getXMLData(data['Home'], 'tag')
skills = model.util.getXMLData(data['Home'], 'skills')

contact = {
    '1-github': model.util.getXMLData(data['Contact'], 'github'),
    '2-mail': model.util.getXMLData(data['Contact'], 'mail'),
    '3-skype': model.util.getXMLData(data['Contact'], 'skype'),
    '4-linkedin': model.util.getXMLData(data['Contact'], 'linkedin'),
    '5-icq': model.util.getXMLData(data['Contact'], 'icq'),
    '6-twitter': model.util.getXMLData(data['Contact'], 'twitter')
}

links = model.util.getXMLData(data['Contact'], 'links')

print view.head.getHead('frontend')
print '<html>'
print view.body.getHomeBody(title, tag, skills, contact, links)
print '</html>'
