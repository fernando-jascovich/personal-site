#!/usr/local/bin/python
#!/usr/bin/python

import os
import sys
from cgi import escape

print "Content-type: text/html"
print
print "<pre>"
print "<strong>Python %s</strong>" % sys.version

keys = os.environ.keys()
keys.sort()

for k in keys:
    print "%s\t%s" % (escape(k), escape(os.environ[k]))

print "</pre>"
