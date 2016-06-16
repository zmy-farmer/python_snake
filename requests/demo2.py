# coding:utf-8
__author__ = 'zhangmengyuan'

"""
requests get post传值
"""
import requests

# payload = {'key1': 'value1', 'key2': 'value2'}
# headers = {'content-type': 'application/json'}
# r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
# print r.url
#
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print r.text


r = requests.get('https://github.com', verify=True)
print r.text