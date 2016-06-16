# coding:utf-8
__author__ = 'zhangmengyuan'

import requests

r = requests.get("http://www.baidu.com")
print type(r)
print r.status_code
print r.encoding
print r.cookies
