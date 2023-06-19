import requests

url="http://www.baidu.com"
requests = requests.get(url)
# 一个类型和六个属性
# Response类型
print(type(requests))
# 设置相应编码的格式
requests.encoding = 'utf-8'
# 以字符串的形式返回网页源码
print(requests.text)
# 返回url地址
print(requests.url)
# 返回二进制数据
print(requests.content)
# 返回状态码
print(requests.status_code)
# 返回头信息
print(requests.headers)