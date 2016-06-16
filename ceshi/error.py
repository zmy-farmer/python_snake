__author__ = 'zhangmengyuan'

import urllib2

request = urllib2.Request("http://blog.csdn.net/cqcre")

try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError,e:
    print e.code
    print e.reason
except urllib2.URLError,e:
    print e.reason
else:
    print response.read()