# -*- coding:utf-8 -*-
# 9787040437928
import urllib
import urllib2
import HTMLParser
import time
import random
import thread
import re
import os
import time
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
html_parser=HTMLParser.HTMLParser()
#
def book_name(message):
    pattern = re.compile('书名:.[^\<]*(?=<)', re.S)
    bname = re.findall(pattern, message)  ##
    if bname==[]:
        file.write("书名：暂无信息\n")
        print ("书名：暂无信息\n")
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
        file.write(txt)
        print txt
def publish_name(message):
    pattern = re.compile('出版社名称.[^\<]*(?=<)', re.S)
    pname = re.findall(pattern, message)  ##
    #print pname[0]
    if pname==[]:
        file.write("出版社名称：暂无信息\n")
        print ("出版社名称：暂无信息\n")
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
        print ("定价：暂无信息\n")
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
        print ("作者：暂无信息\n")
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
        print ("ISBN编号：暂无信息\n")
    else:
        isbn[0].decode('utf-8')
        # print isbn[0]
        pattern = re.compile('(?<=:).*', re.S)
        isbn = re.findall(pattern, isbn[0])
        txt = html_parser.unescape(isbn[0])
        isbn = re.sub(r'\"', ' ', txt)
        txt = "ISBN编号：" + txt+"\n"
        file.write(txt)
        #return isbn
        print txt
def publish_time(message):
    pattern = re.compile('出版时间:.[^\<]*(?=<)', re.S)
    ptime = re.findall(pattern, message)  ##
    if ptime == []:
        file.write("出版时间：暂无信息\n")
        print ("出版时间：暂无信息\n")
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
def getImg(pic,i,new_path):
    t5 = time.time()
    urllib.urlretrieve(pic,new_path+'\%s.jpg'%i)
    t6 = time.time()
    print t6 - t5, "\n"
print"搜索："
data=raw_input()
out=urllib.quote(data)
data = '"' + data + '"'
data = unicode(eval(data), 'utf-8', 'ignore')
print"文件路径："
#way=raw_input()
way='C:/Users/gyd/Desktop/tmaodate'
file=time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
file=file+"_"+data
print file
if os.path.isdir(way):
    new_path = os.path.join(way, file)
    os.mkdir(new_path)
else:
    os.mkdir(way)
    new_path = os.path.join(way, file)
    os.mkdir(new_path)
s="https://s.taobao.com/search?q="+out+"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20171016&cps=yes&cat=33&sort=sale-desc&ie=utf8"
response=urllib2.urlopen(s)
date=response.read()
pattern=re.compile('(?<="comment_url":").[^\"]*(?=")',re.S)
url=re.findall(pattern,date)
pattern=re.compile('(?<="pic_url":").[^\"]*(?=")',re.S)                     #商品照片
picurl=re.findall(pattern,date)
pattern=re.compile('(?<="view_price":").[^\"]*(?=")',re.S)                     #商品照片
view_price=re.findall(pattern,date)
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
    t1=time.time()
    file = open(new_path+ '\date.txt', 'a')
    file.write("第" + str(i)+ "本：\n")
    book_name(message)                                                      #获取书名
    publish_name(message)                                                   #获取出版商
    publish_time(message)                                                   #获取出版日期
    author(message)                                                         #获取作者名
    price(message)                                                          #获取商品价格
    ISBN(message)
    txt="现价："+view_price[i]+"\n"
    file.write(txt)
    pic = "https:" + picurl[i]
    file.write("照片链接："+pic+"\n")
    file.write("\n")
    file.close()
    t2 = time.time()
    print t2-t1,"\n"
    getImg(pic,i,new_path)
    t3 = time.time()
    print t3-t2,"\n"
    t=random.uniform(1,10)
    print t
    time.sleep(t)

    #print picurl[i]
    print"\n"
'''
file=open('C:\Users\gyd\PycharmProjects\untitled\date.txt','a')
file.write(message)
file.close()'''
#                          9787040437928