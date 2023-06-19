# -*- coding: utf-8 -*-
# @Time : 2022/11/12 23:11
# @Author : 悬笔墨客
# @File : 16_解析_jsonpath解析淘票票.py
import json
import jsonpath
import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1668268145775_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'accept':' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9',
    'bx-v':' 2.2.3',
    'cookie':' _m_h5_tk=f6663cc7b65068c9813d6b1762d661a1_1668192010205; _m_h5_tk_enc=fada52344c5a231f01033c0d0dd4f0ad; cna=HJzwG40R5l8CAdONrJu6dbD1; xlly_s=1; t=8232d1945a237d542009fa5f62ac94ba; cookie2=1c435f70fd1b44c570abce085193228b; v=0; _tb_token_=e364515b9fe6d; tb_city=340400; tb_cityName="u7TEzw=="; tfstk=c_LhBkDb9HSQFHgJCp_IldJiFbiAaMoFdU8w7fAmFM8BqJYNTs4bboy83fXKhvr5.; l=eBM4s7mgTyl0TM9fBO5Courza77OzIObzPVzaNbMiInca6MdteliRNCUxMYpSdtjgtfeFetzmSrNYdBmA3Up_giMW_9jisV6mY9w-; isg=BEpKIr-XHeowXpFHdxCT_rKvmzDsO86V3p4LtNSCph02h-hBvMtypMD5l_NbckYt',
    'referer':' https://dianying.taobao.com/index.htm?spm=a1z21.3046609.city.123.2e0d112aLJpyuc&n_s=new&city=340400',
    'sec-ch-ua':' "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'sec-fetch-dest':' empty',
    'sec-fetch-mode':' cors',
    'sec-fetch-site':' same-origin',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with':' XMLHttpRequest'
}
requests = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(requests)
content = response.read().decode('utf-8')
# 得到的json文件多出了不必要的部分
# 使用切片的方法得到有效数据
content = content.split('(')[1].split(')')[0]
# with open('16_解析_jsonpath解析淘票票.json','w',encoding='utf-8') as fp:
#     fp.write(content)

obj = json.load(open('16_解析_jsonpath解析淘票票.json', 'r', encoding='utf-8'))
id = jsonpath.jsonpath(obj,'$..id')
city = jsonpath.jsonpath(obj,'$..regionName')
code = jsonpath.jsonpath(obj,'$..cityCode')
pinyin = jsonpath.jsonpath(obj,'$..pinYin')

# 将list按列存入csv
import csv
rows = zip(id,city,code,pinyin)
with open('城市数据.csv', "w", newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)