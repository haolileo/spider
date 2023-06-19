from selenium import webdriver

# 创建浏览器操作对象
browser = webdriver.Chrome()
# 访问网站
url = 'https://www.jd.com'
browser.get(url)
# page_source获取网页源码
content = browser.page_source
print(content)
