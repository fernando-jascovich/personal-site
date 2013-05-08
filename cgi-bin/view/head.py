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
    if self == 'backend' or self == 'no-js':
        metaTag.append('<meta name="robots" content="noindex">')
    else:
        metaTag.append('<meta name="keywords" content="fernando jascovich web developer programming programmer code geek nerd php ruby python java"')
        metaTag.append('<meta name="description" content="Personal website"')
    metaTag.append('<title>' + os.environ['HTTP_HOST'] + ' | %s</title>' % self)
    return metaTag


def getStyleSheet(self):
    stylesheets = []
    stylesheets.append('<link href="http://fonts.googleapis.com/css?family=Average+Sans|Roboto+Slab" rel="stylesheet" type="text/css">')
    stylesheets.append('<link rel="stylesheet" media="all" href="style.min.css" />')
    stylesheets.append('<!--[if gte IE 9]><style type="text/css">.gradient { filter: none; }</style><![endif]-->')
    return stylesheets


def getScripts(self):
    scripts = []
    scripts.append('<script src="js/jquery-1.9.1.min.js"></script>')
    if self == 'backend':
        scripts.append('<script src="js/backend.min.js"></script>')
    else:
        scripts.append('<script src="js/frontend.min.js"></script>')
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
