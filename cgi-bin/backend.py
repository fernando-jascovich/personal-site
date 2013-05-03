#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

import os
import cgi
import model.util
import view.head
import view.header
import view.body
import view.footer
import md5

print 'Content-type: text/html'
print

filename, fileextension = os.path.splitext(os.path.basename(__file__))
post = cgi.FieldStorage()
page = model.util.BasePage(post.getvalue('token'))

if post.getvalue('token'):
    try:
        class TokenDataModel:
            name = 'token'

        tokenDataModel = model.util.getDataModel(TokenDataModel)

        if post.getvalue('token') != tokenDataModel['token']:
            raise ValueError("Invalid token. You're not really authenticated, don't you?")

    except ValueError as inst:
        print inst
        raise SystemExit()

    savevalues = {}

    for item, value in page.pages.iteritems():
        postvalue = post.getvalue(model.util.sanitize(item))
        if postvalue is not None:
            savevalues[item] = postvalue

    if(len(savevalues) > 0):
        model.util.saveDataModel(page, savevalues)

else:
    class TokenModel:
        name = 'token'
        pages = {
            'token': ''
        }
        values = {
            'token': page.token
        }

    tokenModelInstance = TokenModel()
    model.util.saveDataModel(tokenModelInstance, tokenModelInstance.values)

data = model.util.getDataModel(page)

if post.getvalue('useremail') != None and post.getvalue('token') == None:
    class LoginModel:
        name = 'login'

    logData = model.util.getDataModel(LoginModel())

    try:
        md5Pass = logData[post.getvalue('useremail')]
    except KeyError:
        print 'Your user is not registered on this page.'
        raise SystemExit()

    userpassword = md5.new()
    userpassword.update(post.getvalue('userpassword'))

    if md5Pass == userpassword.hexdigest():
        print view.head.getHead('js')
        print '<html>'
        print view.header.getSimpleHeader(page)
        print view.body.getBackEndBody(page, data)
        print view.footer.getActionsBar(page)
    else:
        print 'The password is incorrect'
        raise SystemExit()
elif post.getvalue('token') != None:
    print view.head.getHead('js')
    print '<html>'
    print view.header.getSimpleHeader(page)
    print view.body.getBackEndBody(page, data)
    print view.footer.getActionsBar(page)
else:
    print view.head.getHead('no-js')
    print '<html>'
    print view.body.getLoginBody(post)

print '</html>'
