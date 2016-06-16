__author__ = 'zhangmengyuan'

import urllib
import urllib2

values = {"username":"ceshi","password":"admin","verify_code":"2277"}
data = urllib.urlencode(values)
url = "http://wechat.weishangtianxia.com/index.php/Admin/Login/checklogin.html"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()