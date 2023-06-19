# -*- coding: utf-8 -*-
# @Time : 2022/11/12 15:55
# @Author : 悬笔墨客
# @File : 15_解析_网页图片综合.py

import urllib.request
from lxml import etree

def get_newurl(page):
    if (page == 1):
        url = 'https://pic.netbian.com/4kmeinv/index.html'
    else:
        url = 'https://pic.netbian.com/4kmeinv/index_'+str(page)+'.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    requests = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(requests)
    content = response.read().decode('gbk')
    tree = etree.HTML(content)
    newurl_list = tree.xpath('/html/body/div[2]/div/div[3]/ul//a/@href')
    return newurl_list

def download(new_url):
    for i in range(len(new_url)):
        url = 'https://pic.netbian.com' + new_url[i]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        requests = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(requests)
        content = response.read().decode('gbk')
        tree = etree.HTML(content)
        url = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@src')
        download_url = 'https://pic.netbian.com' + url[0]
        name = tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@title')
        urllib.request.urlretrieve(url=download_url,filename='E:/mm/'+name[0]+'.jpg')

if __name__ == '__main__':
    start_page = int(input('起始页码：'))
    end_page = int(input('结束页码：'))
    for page in range(start_page,end_page+1):
        new_url = get_newurl(page)
        download(new_url)