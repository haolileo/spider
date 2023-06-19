# -*- coding: utf-8 -*-
# @Time : 2022/10/25 23:15
# @Author : 悬笔墨客
# @File : 06_urllib_get请求的urlencode方法.py
import urllib.parse
import urllib.request
#urlencode的应用场景为多个参数的时候
#https://www.baidu.com/s?wd=周杰伦&sex=男
data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国'
}
base_url='https://www.baidu.com/s?'
data=urllib.parse.urlencode(data)
url=base_url+data       #拼接
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)
#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
