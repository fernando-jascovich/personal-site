# View: header
# -*- coding: UTF-8 -*-


def getSimpleHeader(self):
    header = '<div class="simpleHeader"><ul>%s</ul></div>'

    replacement = []
    for item, val in self.inputs.iteritems():
        replacement.append('<li id="' + val['id'] + '">' + val['name'] + '</li>')

    return header % ''.join(replacement)
