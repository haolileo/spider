# -*- coding: utf-8 -*-
# @Time : 2022/11/10 20:27
# @Author : 悬笔墨客
# @File : 13_urllib_代理.py
import random
import urllib.request

# 代理池
proxies_pool = [
    {'http':'112.14.47.6:52024'},
    {'http':'117.114.149.66:55443'},
    {'http':'121.13.252.62:41564'},
    {'http':'121.13.252.61:41564'}
]
proxies = random.choice(proxies_pool)
print(proxies)

url='https://www.baidu.com/s?tn=49055317_28_hao_pg&ie=utf-8&wd=ip'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}

request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(content)