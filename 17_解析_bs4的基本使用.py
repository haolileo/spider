# -*- coding: utf-8 -*-
# @Time : 2022/11/13 16:12
# @Author : 悬笔墨客
# @File : 17_解析_bs4的基本使用.py
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('17_解析_bs4的基本使用.html',encoding='utf-8'),'lxml')

# 根据标签名来查找节点
# 找到的是第一个符合条件的数据
print(soup.a)
# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# （1）find 返回的是第一个符合条件的数据
print(soup.find('a'))
# 根据title的值找到对应的标签对象
print(soup.find('a',title='百度'))
# class属性比较特殊需要加上下划线
print(soup.find('a',class_='l1'))

# （2）find_all 返回的是一个列表其中包含了所有的标签
print(soup.find_all('a'))
# 如果想要获取到是含有多个标签的数据，那么就需要给所有的标签以列表的形式输入
print(soup.find_all(['a','span']))

# （3）select
# select返回的是一个列表，并且返回的是多个数据
print(soup.select('a'))
# 可以通过.来代表class 我们把这种叫做类选择器
print(soup.select('.l1'))
# 使用#来代表id
print(soup.select('#l2'))