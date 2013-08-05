print 'We can import from the current directory just fine.'
print 'But that may not be all we ever want to do.'
print
print "Here's our sys.path:"
print

import sys
print sys.path

print
print 'We get the current working directory for free,'
print 'or the folder containing the file being interpreted.'
print

try:
    from hypertext import request
except Exception, exc:
    print exc

response = request('GET', 'https://raw.github.com/chbrown/zen/master/readability.txt', '')
print response
