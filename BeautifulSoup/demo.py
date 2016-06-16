# coding:utf-8
__author__ = 'zhangmengyuan'

from bs4 import  BeautifulSoup

html = open("./BeautifulSoup/index.html")
soup = BeautifulSoup(html)

# 格式化打印网页内容
# print soup.prettify()
# 打印标签
# print soup.title
#
# print soup.head
#
# print soup.a
#
# print soup.p

print soup.head.contents



for child in  soup.body.children:
    print child



for child in soup.descendants:
    print child

