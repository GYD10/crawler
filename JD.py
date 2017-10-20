# -*- coding:utf-8 -*-
# 9787040437928
import urllib
import urllib2
import HTMLParser
import time
import random
import thread
import re
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
html_parser=HTMLParser.HTMLParser()

def book_name(message):
    pattern = re.compile('书名:.*>.*(?=<)', re.S)
    bname = re.findall(pattern, message)  ##
    print bname
    if bname==[]:
        file.write("书名：暂无信息\n")
        print ("书名：暂无信息")
    else:
        bname[0].decode('utf-8')
        # print bname[0]
        pattern = re.compile('(?<=:).*', re.S)
        bname = re.findall(pattern, bname[0])
    # print name
        txt = html_parser.unescape(bname[0])
        txt= re.sub(r'\"', ' ', txt)
        txt = '"' + txt + '"'
        txt = unicode(eval(txt), 'utf-8', 'ignore')
        txt = "书名：" + txt+"\n"
        #file.write(txt)
        print txt
def publish_name(message):
    pattern = re.compile('出版社名称.[^\<]*(?=<)', re.S)
    pname = re.findall(pattern, message)  ##
    #print pname[0]
    if pname==[]:
        file.write("出版社名称：暂无信息\n")
        print ("出版社名称：暂无信息")
    else:
        pname[0].decode('utf-8')
        # print pname[0]
        pattern = re.compile('(?<=:).*', re.S)
        pname = re.findall(pattern, pname[0])
    # print name
        txt = html_parser.unescape(pname[0])
        txt = re.sub(r'\"', ' ', txt)
        txt = '"' + txt + '"'
        txt = unicode(eval(txt), 'utf-8', 'ignore')
        txt="出版社名称："+txt+"\n"
        file.write(txt)
        print txt

def price(message):
    pattern = re.compile('定价:.[^\<]*(?=<)', re.S)
    bprice = re.findall(pattern, message)  ##
    if bprice==[]:
        file.write("定价：暂无信息\n")
        print ("定价：暂无信息")
    else:
        bprice[0].decode('utf-8')
        # print bprice[0]
        pattern = re.compile('(?<=:).*', re.S)
        bprice = re.findall(pattern, bprice[0])
    # print name
        txt = html_parser.unescape(bprice[0])
        txt = re.sub(r'\"', ' ', txt)
        txt = '"' + txt + '"'
        txt = unicode(eval(txt), 'utf-8', 'ignore')
        txt = "定价：" + txt+"\n"
        file.write(txt)
        print txt

def author(message):
    pattern = re.compile('作者.[^\<\:\：]*(?=<)', re.S)
    aname = re.findall(pattern, message)  ##
    if aname==[]:
        file.write("作者：暂无信息\n")
        print ("作者：暂无信息")
    else:
        aname[0].decode('utf-8')
        # print aname[0]
        pattern = re.compile('(?<=:).*', re.S)
        aname = re.findall(pattern, aname[0])
    # print aname
        txt = html_parser.unescape(aname[0])
        txt = re.sub(r'\"', ' ', txt)
        txt = '"' + txt + '"'
        txt = unicode(eval(txt), 'utf-8', 'ignore')
        txt = "作者：" + txt+"\n"
        file.write(txt)
        print txt

def ISBN(message):
    pattern = re.compile('ISBN编号:.[^\<]*(?=<)', re.S)
    isbn = re.findall(pattern, message)  ##
    if isbn==[]:
        file.write("ISBN编号：暂无信息\n")
        print ("ISBN编号：暂无信息")
    else:
        isbn[0].decode('utf-8')
        # print isbn[0]
        pattern = re.compile('(?<=:).*', re.S)
        isbn = re.findall(pattern, isbn[0])
        txt = html_parser.unescape(isbn[0])
        isbn = re.sub(r'\"', ' ', txt)
        txt = "ISBN编号：" + txt+"\n"
        file.write(txt)
        return isbn
        print txt

def publish_time(message):
    pattern = re.compile('出版时间:.[^\<]*(?=<)', re.S)
    ptime = re.findall(pattern, message)  ##
    if ptime == []:
        file.write("出版时间：暂无信息\n")
        print ("出版时间：暂无信息")
    else:
        ptime[0].decode('utf-8')
        # print ptime[0]
        pattern = re.compile('(?<=:).*', re.S)
        ptime = re.findall(pattern, ptime[0])
        # print ptime
        txt = html_parser.unescape(ptime[0])
        txt = re.sub(r'\"', ' ', txt)
        txt = '"' + txt + '"'
        txt = unicode(eval(txt), 'utf-8', 'ignore')
        txt = "出版时间：" + txt+"\n"
        file.write(txt)
        print txt

def getImg(pic,isbn):
    #print isbn
    page = urllib.urlopen(pic)
    html = page.read()
    pattern = re.compile('src="(.+?\.jpg)" pic_ext', re.S)
    #pic = re.findall(pattern, html)
    urllib.urlretrieve(pic,'C:\Users\gyd\Desktop\\tmaodate\%s.jpg'%isbn)

def getPage(page):
    response = urllib2.urlopen(page)
    message = response.read().decode('GB18030').encode('utf-8')
    book_name(message)  # 获取书名
    '''
    publish_name(message)  # 获取出版商
    publish_time(message)  # 获取出版日期            工科数学分析
    author(message)  # 获取作者名
    price(message)  # 获取商品价格
    isbn = ISBN(message)'''
print"搜索："
data=raw_input()
out=urllib.quote(data)
s="https://search.jd.com/Search?keyword="+out+"&enc=utf-8&wq="+out+"&pvid=4e3b4f49753f4c95b727cf5c26628c49"
response=urllib2.urlopen(s)
date=response.read()
pattern=re.compile('(?<=p-name">).[^\>]*(?=\>)',re.S)
url=re.findall(pattern,date)
for i in range (0,10):
    pattern=re.compile('(?<=href=").[^\"]*(?=\")',re.S)
    page=re.findall(pattern,url[i])
    page = 'https:' +page[0]
    #page = 'https:' + re.sub(r'item.', '', page[0])
    print page
    getPage(page)

'''
pattern=re.compile('(?<="pic_url":").[^\"]*(?=")',re.S)                     #商品照片
picurl=re.findall(pattern,date)
for i in range(0,10):
    pattern=re.compile('http.*:',re.S)
    test=re.findall(pattern,url[i])
    if test==[]:
        url[i]='https:'+re.sub(r'\\u003d','=',url[i])
    else:
        url[i] =re.sub(r'\\u003d', '=', url[i])
    url[i] = re.sub(r'\\u0026', '&', url[i])
    page=url[i]
    print page
    response = urllib2.urlopen(page)
    message = response.read().decode('GB2312').encode('utf-8')              #店铺源码
    #print message
    file = open('C:\Users\gyd\Desktop\\tmaodate\date.txt', 'a')
    book_name(message)                                                      #获取书名
    publish_name(message)                                                   #获取出版商
    publish_time(message)                                                   #获取出版日期
    author(message)                                                         #获取作者名
    price(message)                                                          #获取商品价格
    isbn=ISBN(message)                                                      #获取ISBN
    pic="https:"+picurl[i]
    getImg(pic,isbn)                                                        #获取封面
    file.write("照片链接："+pic+"\n")
    file.write("\n")
    file.close()
    t=random.uniform(1,10)
    time.sleep(t)
    #print picurl[i]
    print"\n"

file=open('C:\Users\gyd\PycharmProjects\untitled\date.txt','a')
file.write(message)
file.close()''''''
#                          9787040437928
'''