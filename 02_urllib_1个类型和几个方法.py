# -*- coding: utf-8 -*-
# @Time : 2022/10/24 11:40
# @Author : 悬笔墨客
# @File : 02_urllib_1个类型和几个方法.py
import urllib.request

url='http://www.baidu.com'
response=urllib.request.urlopen(url)

#response是HTTPResponse类型的数据
type=type(response)
print(type)

#read里加数字代表读取的字节数
content=response.read(5)
print(content)

#返回状态码      如果是200说明没有问题，若是418之类的则存在问题
print(response.getcode())

#返回的是url地址
print(response.geturl())

#返回的是状态信息
print(response.getheaders())