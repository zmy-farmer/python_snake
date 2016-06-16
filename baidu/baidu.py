# _*_ coding:utf-8 _*_
__author__ = 'zhangmengyuan'

import urllib
import urllib2
import re

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

#百度贴吧爬虫类
class BDTB:

    #初始化 传入基地址和是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_LZ=' + str(seeLZ)
        self.tool = Tool()
    #传入页码 获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u"连接百度贴吧失败,失败原因" + e.reason
                return None

    #获取帖子标题
    def getTitle(self):
        page_content = self.getPage(1)
        ze = '<h3 class="core_title_txt.*?>(.*?)</h3>'
        pattern = re.compile(ze,re.S)
        result = re.search(pattern,page_content)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取帖子页数
    def getPageNum(self):
        page_content = self.getPage(1)
        ze = '<li class="l_reply_num.*?</span>.*? <span .*?>(.*?)</span>'
        pattern = re.compile(ze,re.S)
        result = re.search(pattern,page_content)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取每一楼层的内容 并传入页面内容
    def getContent(self,page):
        ze = '<div id="post-content_.*?>(.*?)</div)'
        pattern = re.compile(ze,re.S)
        items = re.findall(pattern,page)
        for item in items:
            print item
        print self.tool.replace(item[1])


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getPageNum()
