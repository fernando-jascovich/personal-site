# View: footer
# -*- coding: UTF-8 -*-


def getActionsBar(page):
    returnHtml = []
    returnHtml.append('<div class="actionBar">')
    returnHtml.append('<ul>')
    returnHtml.append('<li id="save">Guardar</li>')
    returnHtml.append('</ul>')
    returnHtml.append('</div>')
    return ''.join(returnHtml)
