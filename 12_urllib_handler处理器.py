# -*- coding: utf-8 -*-
# @Time : 2022/11/8 23:40
# @Author : 悬笔墨客
# @File : 12_urllib_handler处理器.py
# 需求：使用handler来访问百度 获取网页源码
import urllib.request

url='http://www.baidu.com'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}

request = urllib.request.Request(url=url, headers=headers)
# 获取handler对象
handler = urllib.request.HTTPHandler()
# 获取opener对象
opener = urllib.request.build_opener(handler)
# 调用open方法
response = opener.open(request)
content = response.read().decode('utf-8')
print(content)
