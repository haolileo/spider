# -*- coding: utf-8 -*-
# @Time : 2022/11/13 10:52
# @Author : 悬笔墨客
# @File : B站电影排行榜.py
import urllib.request
from lxml import etree

url = 'https://www.bilibili.com/v/popular/rank/movie?from_spmid=666.7.hotlist.more'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
requests = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(requests)
content = response.read().decode('utf-8')
tree = etree.HTML(content)
name_list = tree.xpath('//div[@class="info"]/a/text()') # 有时候xpath从网页上返回的类型可能是element类型就需要加上/text()进行转换
url_list = tree.xpath('//div[@class="info"]/a/@href')
release_time = tree.xpath('//div[@class="detail"]/span/text()')
print(release_time)
# for i in range(len(url_list)):
#     url_list[i] = url_list[i].split('//')[1]
# release_time = tree.xpath('//div[@class="detail"]/span/text()')
# for i in range(len(release_time)):
#     release_time[i] = release_time[i].split('\n              ')[1].split('\n')[0]
# count = tree.xpath('//div[@class="info"]//span/text()')
# play = []
# for i in range(1,len(count),3):
#     play.append(count[i])
# for i in range(len(play)):
#     play[i] = play[i].split('\n                ')[1].split('\n')[0]
# collection = []
# for i in range(2,len(count),3):
#     collection.append(count[i])
# for i in range(len(collection)):
#     collection[i] = collection[i].split('\n                ')[1].split('\n')[0]
# 将list按列存入csv
# import csv
# rows = zip(name_list,url_list,release_time)#,play,collection
# with open('B站电影排行榜（1）.csv', "w", newline='') as f:
#     writer = csv.writer(f)
#     for row in rows:
#         writer.writerow(row)