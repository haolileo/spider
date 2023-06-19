# -*- coding: utf-8 -*-
# @Time : 2022/10/24 10:16
# @Author : 悬笔墨客
# @File : 01_urllib_基本使用.py
import urllib.request

#使用urllib来访问百度首页
#定义一个url
url="http://www.baidu.com"
#模拟浏览器向服务器发送请求,得到相应结果
response=urllib.request.urlopen(url)
#获取相应中的页面源码
#read方法所返回的是字节形式的二进制数据，所以需要对其进行解码
print(response.read().decode('utf-8'))