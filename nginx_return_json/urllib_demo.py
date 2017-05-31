#!/usr/bin/env python

import urllib2

ROOT_URL = 'http://127.0.0.1:8080'

req = urllib2.Request(ROOT_URL + "/error")

try:
    response = urllib2.urlopen(req)
except urllib2.HTTPError as e:
    print "Exception: {0}".format(e)
    print "Error code: {0}".format(e.code)
    print "Error message: {0}".format(e.read())
