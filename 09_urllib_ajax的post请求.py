# -*- coding: utf-8 -*-
# @Time : 2022/10/29 21:54
# @Author : 悬笔墨客
# @File : 09_urllib_ajax的post请求.py
import urllib.request
import urllib.parse

def creat_request(page):
    base_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data={
        'cname': '合肥',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data=urllib.parse.urlencode(data).encode('utf-8')
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    requests = urllib.request.Request(url=base_url,data=data,headers=headers)
    return requests

def get_content(requests):
    response = urllib.request.urlopen(requests)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('kfc'+str(page)+'.json','w',encoding='utf-8') as fp:
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
        down_load(page, content)