'''This file is a slim wrapper around part of the awkward urllib2 module'''
import sys
import urllib2


def request(method, url, data, headers=None):
    req = urllib2.Request(url, data, headers or {})
    req.get_method = lambda: method

    res = urllib2.urlopen(req)

    print >> sys.stderr, '[response]', res.getcode(), res.geturl()

    return res.read()
