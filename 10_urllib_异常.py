# -*- coding: utf-8 -*-
# @Time : 2022/11/6 12:28
# @Author : 悬笔墨客
# @File : 10_urllib_异常.py
import urllib.request
import urllib.error
url = 'https://blog.csdn.net/m0_52634705/article/details/116187237'     # 出现http的错误，比如后面数字出现变动
url = 'https://www.goudan111.com'   # 出现网页url的错误
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

try:
    requests = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(requests)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print("服务器正在升级，请稍后！！")
except urllib.error.URLError:
    print("出了一点小差错!!")