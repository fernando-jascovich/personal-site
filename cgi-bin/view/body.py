# View: body
# -*- coding: UTF-8 -*-


def getBackEndBody(self, data):
    returnHtml = []
    returnHtml.append('<form action="backend" method="post" id="backendForm">')

    for key, value in self.inputs.iteritems():
        returnHtml.append(getTextAreaField(value['id'], value['name'], data[key]))

    returnHtml.append('<div class="spacer"></div>')
    returnHtml.append(('<input type="hidden" name="token" value="%s" />' %
        self.token))
    returnHtml.append('</form>')
    return ''.join(returnHtml)


def getInputField(id, name, type, val):
    labelHtml = '<label for="%s">%s</label>' % (id, name)
    inputHtml = ('<input type="%s" id="%s" name="%s" value="%s" />' %
        (type, id, id, val))
    return '<div>' + labelHtml + inputHtml + '</div>'


def getTextAreaField(id, name, val):
    inputHtml = ('<textarea id="%s" name="%s">%s</textarea>' %
        (id, id, val))
    return '<div>' + inputHtml + '</div>'


def getLoginBody(postdata):
    returnHtml = []
    returnHtml.append('<div class="loginFormContainer">')
    returnHtml.append('<form action="backend" method="post" id="loginForm">')
    returnHtml.append('<input type="text" name="useremail" value="" />')
    returnHtml.append('<input type="password" name="userpassword" value="" />')
    returnHtml.append('<input type="submit" value="Log in" />')
    returnHtml.append('</form>')
    returnHtml.append('</div>')
    return ''.join(returnHtml)
