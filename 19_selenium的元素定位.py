from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://www.baidu.com'
browser.get(url)
# 元素定位
# 根据id来找到对象
botton1 = browser.find_element(By.ID,'su')
# 根据标签属性的属性值来获取对象
botton2 = browser.find_element(By.NAME,'wd')
# 根据xpath来定位对象
botton3 = browser.find_element(By.XPATH,'//input[@id="su"]')
# 根据标签名来获取对象
botton4 = browser.find_elements(By.TAG_NAME,'input')
# 使用bs4的语法来实现定位
botton5 = browser.find_elements(By.CSS_SELECTOR,'#su')
# 使用链接文本来实现定位
botton6 = browser.find_elements(By.LINK_TEXT,'地图')
print(botton1,botton2,botton3,botton4,botton5,botton6)