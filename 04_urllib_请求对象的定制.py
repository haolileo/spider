# -*- coding: utf-8 -*-
# @Time : 2022/10/24 12:45
# @Author : 悬笔墨客
# @File : 04_urllib_请求对象的定制.py
import urllib.request

url='https://www.baidu.com'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
#因为urlopen方法不能存储字典类型，所以需要用得到请求对象的定制
#因为Requests参数顺序的问题不能直接填写url和headers，所以需要关键字来传递参数
request=urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))