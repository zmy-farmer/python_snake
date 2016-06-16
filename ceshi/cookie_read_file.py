__author__ = 'zhangmengyuan'
import urllib2
import cookielib

cookie = cookielib.MozillaCookieJar()

cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)

req = urllib2.Request("Http://www.baidu.com")

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)

response = opener.open(req)

print response.read()