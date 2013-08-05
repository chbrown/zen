'''This file is aliased to run-sanity-example, by the way.'''

from styling import colors


def main():
    print colors.cyan('So'), colors.yellow('cool'), ',', colors.blue('right'), '?'

    print
    print "But that's a bit dark, let's add some yellow"
    print
    print 's/black/yellow/ above'
    print
    print 'And then add this to colors.py:'
    print
    print 'def yellow(message):'
    print """    return '\\x1b[33m' + message + '\\x1b[39m'"""
    print
    print 'And then rerun:'
    print
    print '    run-sanity-example'
    print
    print 'Still no yellow? Try'
    print
    print '    python setup.py develop'
    print '    run-sanity-example'
    print
