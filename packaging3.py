try:
    from hyper import text
except Exception, exc:
    print exc

print
print "Let's get our IP address"
print

print text.try_get('http://v4.icanhazip.com')

print 'Trying a slightly more complex dependency -- text.try_get will print a'
print 'reddened error message if not successful'
print

print text.try_get('https://raw.github.com/chbrown/zen/master/missing.exe')

print
print "So far so good, but we might get carried away."
print

print 'Next up:'
print
print '    cd hyper/'
print '    ./get.py http://v4.icanhazip.com'
