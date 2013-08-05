'''This file is a slim wrapper around part of the awkward urllib2 module'''
import urllib2


def request(method, url, data, headers=None):
    req = urllib2.Request(url, data, headers)
    req.get_method = lambda: method

    res = urllib2.urlopen(req)

    return res.read()
