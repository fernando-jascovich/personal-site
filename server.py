#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from wsgiref.simple_server import make_server, demo_app

httpd = make_server('127.10.54.1', 7025, demo_app)

print "Content-Type: text/plain;charset=utf-8"
print
print "Serving HTTP on port 7025..."

# Respond to requests until process is killed
##httpd.serve_forever()

# Alternative: serve one request, then exit
httpd.handle_request()
