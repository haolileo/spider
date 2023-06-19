info={"name":"master","age":18}
print(info["age"])
print(info.get("name"))
print(info)
#增
info["id"]=123456
print(info)

#删
'''
#【del】删除指定元素
del info["id"]
print(info)
#【clear】清空
info.clear()
print(info)
'''

#改
info["age"]=20
print(info)

#查
# print(info.keys())
# print(info.values())
# print(info.items())

#遍历所有的键值对
for key,value in info.items():
    print(key,value)
