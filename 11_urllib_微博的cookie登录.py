# -*- coding: utf-8 -*-
# @Time : 2022/11/6 12:53
# @Author : 悬笔墨客
# @File : 11_urllib_微博的cookie登录.py
import urllib.request
# 适用场景：数据采集的时候需要绕过登录进入到某个页面
# 个人信息页面是utf-8,但还是报了编码错误,是因为没有进入个人信息页面是跳转到登录页面
# 因为登录页面并不是utf-8所以会报编码错误
url = 'https://weibo.cn/7508933403/info'
headers={
    # cookie中携带着登录信息，如果有登录之后的cookie那么我们就可以使用该cookie进入各种页面
    'cookie':'_T_WM=76480021925; SCF=ArO-W0xIkMp7q8-8o1XoLj39i1Jh3MSb3DHAgTjg0O2cOLm9uImFWGp2qOJUNDvvIEUnpLEU_zwy9xKVWx9A6Nc.; SUB=_2A25OYzbxDeRhGeFL61oY8y3Iyz-IHXVtrFq5rDV6PUJbktANLXfbkW1NQp9S0IcVyhqWA84mcLQvz1h-00MGtT7X; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFwVDMfj.6Ji11G.oVF1x-5JpX5oz75NHD95QNSK5R1Ke0Sh50Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0-71h.0e0B7e7tt; ALF=1670304673; MLOGIN=1',
    # referer 用来判断当前路径是不是由上一级路径进来的，可以用来作为图片的防盗链
    'referer':'https://weibo.cn/',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'
}
requests = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(requests)
content = response.read().decode('utf-8')
# 将数据保存到本地
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)