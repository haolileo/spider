# -*- coding: utf-8 -*-
# @Time : 2022/10/26 0:00
# @Author : 悬笔墨客
# @File : 07_urllib_post请求.py
import json
import urllib.request
import urllib.parse
url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers={
    # 'Accept':' */*',
    # 'Accept-Encoding':' gzip, deflate, br',解码方式要按照utf-8
    # 'Accept-Language':' zh-CN,zh;q=0.9',
    # 'Connection':' keep-alive',
    # 'Content-Length':' 135',
    # 'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':' BIDUPSID=77D04A5C24433FE840B4CB1679842A74; PSTM=1615373036; __yjs_duid=1_1370568de110b0962fabdc21d6911d6c1618068150020; BAIDUID=000D79B7F250CEFC5143DAC155AE483F:FG=1; BDUSS=xVeTJheUhBNXZpTFdhcFJmcVdSY0ZiaU50VkZPMVpOcHlHVEpYOVJuTi1VVTFqSVFBQUFBJCQAAAAAAAAAAAEAAABL4z9gbWFzdGVyYmFrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7EJWN-xCVjM2; MCITY=-250%3A; BDUSS_BFESS=xVeTJheUhBNXZpTFdhcFJmcVdSY0ZiaU50VkZPMVpOcHlHVEpYOVJuTi1VVTFqSVFBQUFBJCQAAAAAAAAAAAEAAABL4z9gbWFzdGVyYmFrAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7EJWN-xCVjM2; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=000D79B7F250CEFC5143DAC155AE483F:FG=1; BA_HECTOR=a42lal04ak840la08g0kbu4b1hlnljq1b; ZFY=ZyR4Aq1W7q5MOd3nEuvm2LFALQaVWEHRGbHoX3d8FcU:C; RT="z=1&dm=baidu.com&si=cfppt2505p8&ss=l9sirr5j&sl=4&tt=57v&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5df&ul=6e7&hd=6fn"; BDRCVFR[S_ukKV6dOkf]=mk3SLVN4HKm; delPer=0; PSINO=3; H_PS_PSSID=36544_37636_37516_36921_37584_36885_34813_37627_36805_36786_37537_37497_37576_26350_22158; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1666712975,1667017122; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1667017138; ab_sr=1.0.1_NjYzM2NlOTQ1NDJjNTA3N2FlMGM0YTJiYjI2MjBjZGRhNDI4NThjYmNiMWNmMDRkYTgzZmE5MGM3ZGI2NmMxYTY1Y2NjMzM5MDM2MDIzZGUyYTdlOTA4YzNkOTYyN2FiZWI1MzQ2NzFkYjQ2M2I3ODdiMjYxNTYyZmMwMjRhNjc2ZTUwMzg2ZmI1NTkyOTlhODA5NjlkNGY4MTc1OGVmYmE3MDE4YTNiNDhhNTRhN2E0ZTkxZWNmZGVmYzAyZjcw',
    # 'Host':' fanyi.baidu.com',
    # 'Origin':' https://fanyi.baidu.com',
    # 'Referer':' https://fanyi.baidu.com/translate?query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    # 'sec-ch-ua':' ";Not A Brand";v="99", "Chromium";v="94"',
    # 'sec-ch-ua-mobile':' ?0',
    # 'sec-ch-ua-platform':' "Windows"',
    # 'Sec-Fetch-Dest':' empty',
    # 'Sec-Fetch-Mode':' cors',
    # 'Sec-Fetch-Site':' same-origin',
    # 'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.178.400 QQBrowser/11.2.5170.400',
    # 'X-Requested-With':' XMLHttpRequest'
}
data={
    'from':'en',
    'to':'zh',
    'query':'love',
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'198772.518981',
    'token':'a3115c6f1adbd0f5b2280e6935929ca8',
    'domain':'common'
}
#post请求的参数必须进行编码并且要调用encode编码
data=urllib.parse.urlencode(data).encode('utf-8')
#请求对象的定制
request=urllib.request.Request(url=url,data=data,headers=headers)
#模拟浏览器发送请求给服务器
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
obj=json.loads(content)
print(obj)