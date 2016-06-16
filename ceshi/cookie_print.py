__author__ = 'zhangmengyuan'
import urllib2
import cookielib

#cookie basic oprate

cookie = cookielib.CookieJar()

headler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(headler)

response = opener.open("http://www.baidu.com")

for item in cookie:
    print 'name =' + item.name
    print 'value = ' + item.value

