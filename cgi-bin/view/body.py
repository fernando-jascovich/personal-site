# View: body
# -*- coding: UTF-8 -*-

import re


def getBackEndBody(self, data):
    returnHtml = []
    returnHtml.append('<body class="backend">')
    returnHtml.append('<form action="backend" method="post" id="backendForm">')

    for key, value in self.inputs.iteritems():
        returnHtml.append(getTextAreaField(value['id'], value['name'], data[key]))

    returnHtml.append('<div class="spacer"></div>')
    returnHtml.append(('<input type="hidden" name="token" value="%s" />' %
        self.token))
    returnHtml.append('</form>')
    returnHtml.append('</body>')
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


def getMainPage(title, tag, skills):
    returnHtml = []
    returnHtml.append('<div id="home" class="mainContainer">')
    returnHtml.append('<div class="computer">')
    returnHtml.append('<div class="computerBackground">')
    returnHtml.append('<div id="console" class="skills">%s</div>' % skills)
    returnHtml.append('</div>')
    returnHtml.append('<div class="led"></div>')
    returnHtml.append('<div class="icon"></div>')
    returnHtml.append('</div>')
    returnHtml.append('<div class="side">')
    returnHtml.append('<div class="title">%s</div>' % title)
    returnHtml.append('<div class="tag">%s</div>' % tag)
    returnHtml.append('<div id="contactLink" class="arrow"></div>')
    returnHtml.append('</div>')
    returnHtml.append('</div>')
    return ''.join(returnHtml)


def getContactPage(contactData):
    returnHtml = []
    returnHtml.append('<div id="contact" class="contactContainer">')
    returnHtml.append('<div class="contactItemContainer">')
    returnHtml.append('<div id="homeLink" class="homeArrow"></div>')
    #for key, value in contactData.iteritems():
    #   returnHtml.append('<div class="item"><span class="link %s"></span><span class="text">%s</span></div>' % (key, value))
    for item in sorted(contactData):
        className = re.sub(r'\d+-', r'', item)
        returnHtml.append('<div class="item"><span class="link %s"></span><span class="text">%s</span></div>' % (className, contactData[item]))
    returnHtml.append('</div>')
    returnHtml.append('</div>')
    return ''.join(returnHtml)


def getLinksSection(links):
    linksDict = links.split(',')
    returnHtml = []
    returnHtml.append('<div class="linksContainer">')
    returnHtml.append('<div class="links">')
    returnHtml.append('<div class="linksItself">')
    for item in linksDict:
        returnHtml.append('<a href="%s" target="_blank">%s</a><br />' % (item, item))
    returnHtml.append('</div>')
    returnHtml.append('<div id="links" class="linksButton">i</div></div>')
    returnHtml.append('</div>')
    return ''.join(returnHtml)


def getHomeBody(title, tag, skills, contactData, links):
    returnHtml = []
    returnHtml.append('<body class="frontend">')
    returnHtml.append(getLinksSection(links))
    returnHtml.append('<div class="verticalFloater"></div>')
    returnHtml.append(getMainPage(title, tag, skills))
    returnHtml.append(getContactPage(contactData))
    returnHtml.append('</body>')
    return ''.join(returnHtml)
