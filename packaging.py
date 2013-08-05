print 'I may well have several files in my project at this point'
print 'and I feel like I keep copying and pasting code to do the same thing'
print 'even though I don\'t want my code all in one big file'
print

try:
    print 'Can we just `import style`?'
    from style import colors
    print
    print colors.redden('Import success!')
    print
    print 'Next up: python packaging2.py'
except Exception, exc:
    print 'Nope: "%s". Maybe try:' % exc
    print
    print '    touch style/__init__.py'
