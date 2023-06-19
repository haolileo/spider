# -*- coding: utf-8 -*-
# @Time : 2022/10/24 12:01
# @Author : 悬笔墨客
# @File : 03_urllib_下载.py
import urllib.request
'''
#下载网页
url_page='http://www.baidu.com'
#url代表的是下载的路径，filename代表的是文件名
urllib.request.urlretrieve(url_page,'baidu.html')
'''
'''
#下载图片
url_img='https://img0.baidu.com/it/u=3394852584,4163708711&fm=253&app=53&size=w500&n=0&g=0n&f=jpeg?sec=1669177864&t=59cbca48ed5dd9574c3a1f6e51239e90'
urllib.request.urlretrieve(url_img,'习近平.jpg')
'''
'''
#下载视频
url_movie='https://vd2.bdstatic.com/mda-njg2v8dtxh4yd0bh/sc/cae_h264/1665972315755820356/mda-njg2v8dtxh4yd0bh.mp4?v_from_s=hkapp-haokan-suzhou&amp;auth_key=1666587868-0-0-7f759229b00717f4a2c56661b0ef8fc2&amp;bcevod_channel=searchbox_feed&amp;pd=1&amp;cd=0&amp;pt=3&amp;logid=2068511707&amp;vid=9410008365167324209&amp;abtest=104959_1&amp;klogid=2068511707'
urllib.request.urlretrieve(url_movie,'二十大.mp4')
'''
