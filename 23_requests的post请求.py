# -*- coding: utf-8 -*-
# @Time    : 2022/12/17 14:35
# @Author  : 悬笔墨客
# @File    : 寒假06_requests的post请求.py
import json
import requests
post_url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
data = {
    'kw':'eye'
}
response = requests.post(url=post_url,headers=headers,data=data)
content = response.text
obj = json.loads(content)
print(obj)

# 总结：
# （1）post请求不需要编解码
# （2）post请求参数是data
# （3）不需要请求对象的定制