# -*- coding: utf-8 -*-
# @Time : 2022/10/30 16:18
# @Author : 悬笔墨客
# @File : 文件的序列化与反序列化.py
import json

# 两种序列化的方法
# dumps()
fp = open('test.txt','w')
# 默认状态下对象是无法写入到文件中去的
list = ['zhangsan','lisi']
# 将python对象变成json字符串
name = json.dumps(list)
fp.write(name)
fp.close()

# dump()
fp = open('test.txt','w')
list = ['zhangsan','lisi','wangwu']
json.dump(list,fp)
fp.close()


# 两种反序列化的方法
# loads()
fp = open('test.txt','r')
content = fp.read()
result = json.loads(content)

# load()
fp = open('test.txt','r')
result = json.load(fp)
print(type(result))
fp.close()