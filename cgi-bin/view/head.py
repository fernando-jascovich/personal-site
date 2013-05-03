# meta tags
# -*- coding: UTF-8 -*-

import os


def getDoctype(self):
    doctype = []
    doctype.append('<!DOCTYPE html>')
    doctype.append('<html>')
    return doctype


def getMetaTags(self):
    metaTag = []
    metaTag.append('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />')
    metaTag.append('<meta name="viewport" content="width=device-width, initial-scale=1" />')
    metaTag.append('<title>' + os.environ['HTTP_HOST'] + ' | %s</title>' % self)
    return metaTag


def getStyleSheet(self):
    stylesheets = []
    stylesheets.append('<link href="http://fonts.googleapis.com/css?family=Average+Sans|Roboto+Slab" rel="stylesheet" type="text/css">')
    stylesheets.append('<link rel="stylesheet" media="all" href="style.css" />')
    stylesheets.append('<!--[if gte IE 9]><style type="text/css">.gradient { filter: none; }</style><![endif]-->')
    return stylesheets


def getScripts(self):
    scripts = []
    scripts.append('<script src="js/jquery-1.9.1.min.js"></script>')
    scripts.append('<script src="js/main.js"></script>')
    return scripts


def getHead(self):
    head = []
    head.append('<head>')
    head.append(''.join(getDoctype(self)))
    head.append(''.join(getMetaTags(self)))
    head.append(''.join(getStyleSheet(self)))
    if self != 'no-js':
        head.append(''.join(getScripts(self)))
    head.append('</head>')
    return ''.join(head)