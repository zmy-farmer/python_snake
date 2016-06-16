__author__ = 'zhangmengyuan'

import urllib2

request = urllib2.Request("http://blog.csdn.net/cqcre")

try:
    response = urllib2.urlopen(request)
except urllib2.URLError,e:
  if hasattr(e,'code'):
      print e.code
  if hasattr(e,"reason"):
      print e.reason
else:
    print response.read()