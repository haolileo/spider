# -*- coding: utf-8 -*-
# @Time    : 2022/12/17 15:22
# @Author  : 悬笔墨客
# @File    : 寒假08_requests的cookie登录.py
import requests

url = 'https://www.ptpress.com.cn/login'     # 表单提交入口
# 使用Cookie登录方法实现模拟登录lh*20030304*
cookie = 'acw_tc=2760778616712630332746586ecfa3a2f5b580d1d1adc2abff6bd48abe35ef; JSESSIONID=F0905F1CB92F3628BE5731A0863E2432; gr_user_id=227fc491-df59-465e-b51b-e2f1348f3eb8; gr_session_id_9311c428042bb76e=361c223f-ce3c-4972-8d96-fa7addd35e51; gr_session_id_9311c428042bb76e_361c223f-ce3c-4972-8d96-fa7addd35e51=true'
Cookies = {}

# 将Cookie转成字典结构
for i in cookie.split(';'):
    key, value = i.split('=')
    Cookies[key] = value

host = 'https://www.ptpress.com.cn/'        # 网站主页
rq = requests.get(host, cookies=Cookies)    # 以登录状态获取目标网站数据
print(rq.text)