import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(1)

# input = browser.find_element(By.ID,'su')
# # 获取标签属性
# print(input.get_attribute('value'))
# # 获取标签名
# print(input.tag_name)
# # 获取元素文本
# a = browser.find_element(By.LINK_TEXT,'新闻')
# print(a.text)

# 获取文本框对象
input = browser.find_element(By.ID,'kw')
# 在文本框中输入关键字
input.send_keys('周杰伦')
time.sleep(1)

# 获取百度一下的按钮
botton = browser.find_element(By.ID,'su')
botton.click() # 点击
time.sleep(1)

# 滑到底部
js_bottom = 'window.scrollTo(0, document.body.scrollHeight)'
browser.execute_script(js_bottom)
time.sleep(1)

# 点击下一页
next_page = browser.find_element(By.XPATH,'//a[@class="n"]')
next_page.click()
time.sleep(1)

# 回到上一页
browser.back()
# 回退
browser.forward()
time.sleep(1)

browser.close()
