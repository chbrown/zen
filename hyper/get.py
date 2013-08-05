#!/usr/bin/env python
import sys
import text

url = sys.argv[-1]
print
print 'GETting ' + url
print
print text.try_get(url)

print 'Awesome, no problem, now try'
print
print '    ./get.py https://raw.github.com/chbrown/zen/master/missing.exe'
