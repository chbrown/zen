print 'I may well have several files in my project at this point'
print 'and I feel like I keep copying and pasting code to do the same thing'
print 'even though I don\'t want my code all in one big file'

try:
    from hypertext import request
except Exception, exc:
    print "hypertext, what's that?"
    print exc


try:
    print 'Relative imports are impolite, but we can try...'
    from .hypertext import request
except Exception, exc:
    print 'No dice'
    print exc

print '# sys.path hacks:'

import sys
sys.path.insert(0, '.')

from hypertext import request

response = request('GET', 'https://raw.github.com/chbrown/zen/master/readability.txt', None)
