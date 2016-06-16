__author__ = 'zhangmengyuan'
import urllib2
import cookielib

#cookie basic oprate
filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)

headler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(headler)

response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True,ignore_expires=True)

