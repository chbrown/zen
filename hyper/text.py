import urllib2


def try_get(url):
    try:
        res = urllib2.urlopen(url)
    except urllib2.HTTPError, http_exception:
        try:
            from style import colors
            print colors.redden('HTTP failure! %s' % http_exception)
        except ImportError, exc:
            print 'WTF, it worked before! "%s"' % exc
            print
            print "Let's try something else"
            print
            print '    cd ..'
            print '    mv .sanity sanity'
            print
            raise

    return res.read()
