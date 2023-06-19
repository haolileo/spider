# -*- coding: utf-8 -*-
# @Time    : 2022/12/17 16:32
# @Author  : 悬笔墨客
# @File    : 京东秒杀.py
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器操作对象
browser = webdriver.Chrome()
# 访问网站
url = 'https://miaosha.jd.com/'
browser.get(url)
# page_source获取网页源码
text = browser.page_source
html = etree.HTML(text)
name = html.xpath('//div/ul/li//h4/text()')
price = html.xpath('//div/ul/li/div/span/span[1]/i/text()')
sale = html.xpath('//div/ul/li/div/span/span[2]/i[1]/text()')
time.sleep(2)
browser.close()
# 将list按列存入csv
import csv
rows = zip(name,price,sale)
with open('京东秒杀.csv', "w", newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)