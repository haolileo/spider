# -*- coding: utf-8 -*-
# @Time : 2022/10/29 15:18
# @Author : 悬笔墨客
# @File : 08_urllib_ajax的get请求.py
import urllib.request
import urllib.parse

def creat_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&'
    data={
        'start':(page-1)*20,
        'limit':20
    }
    data=urllib.parse.urlencode(data)
    url=base_url+data
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    requests = urllib.request.Request(url=url,headers=headers)
    return requests

def get_content(requests):
    response = urllib.request.urlopen(requests)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('douban'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

# 程序的入口
if __name__ == '__main__':
    start_page = int(input('起始页码：'))
    end_page = int(input('结束页码：'))
    for page in range(start_page,end_page+1):
        # 每一页请求对象的定制
        requests = creat_request(page)
        # 获取响应的数据
        content = get_content(requests)
        # 下载
        down_load(page,content)