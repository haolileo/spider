# -*- coding: utf-8 -*-
# @Time    : 2022/12/20 21:47
# @Author  : 悬笔墨客
# @File    : getIP.py
# coding=utf-8
import requests
import time
# 请求地址
targetUrl = "http://api.shenlongip.com/ip"
params = {
    'key':'7x6e88co',
    'count':1,
}
resp = requests.get(targetUrl,params=params)
print(resp.text)