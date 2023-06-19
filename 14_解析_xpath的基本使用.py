# -*- coding: utf-8 -*-
# @Time : 2022/11/12 0:28
# @Author : 悬笔墨客
# @File : 14_解析_xpath的基本使用.py
from lxml import etree

# xpath解析
# 本地文件            etree.parse
# 服务器响应数据       etree.HTML

# xpath来解析本地文件
tree = etree.parse('14_解析_xpath的基本使用.html')

# tree.xpath('xpath路径')

# 查找ul下面的li
li_list = tree.xpath('//body/ul/li')

# 查找所有具有id属性的标签,使用text()可以查询标签中的内容
id_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 查找id为l1的li标签的class属性值
li_class = tree.xpath('//ul/li[@id="l1"]/@class')

# 模糊查询id中包含l的li标签
mohu_list = tree.xpath('//ul/li[contains(@id,"l")]')

# 判断列表的长度
print(li_list,id_list,li_class,mohu_list)

