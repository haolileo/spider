# -*- coding: utf-8 -*-
# @Time : 2022/10/24 19:32
# @Author : 悬笔墨客
# @File : 05_urllib_get请求的quote方法.py
import urllib.request
import urllib.parse
#获取网页源码
url='https://cn.bing.com/search?q='
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}

#将文字变为Unicode编码的格式，需要用到urllib.parse.quote方法
name=urllib.parse.quote('周杰伦')
url=url+name

#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))