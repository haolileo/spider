from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

# 自动打开浏览器并且最大化窗口
driver = webdriver.Chrome()
driver.maximize_window()

# 自动输入淘宝网址，并根据链接文本选择元素，点击界面上的登录按钮
driver.get('https://www.taobao.com')
if driver.find_element(By.LINK_TEXT, '亲，请登录'):
    driver.find_element(By.LINK_TEXT, '亲，请登录').click()
    print("请在15秒内完成扫码")
    time.sleep(15)
    # 打开购物车列表首页
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
# 点击全选按钮
if driver.find_element(By.ID, 'J_SelectAll1'):
    driver.find_element(By.ID, 'J_SelectAll1').click()

now = datetime.datetime.now()
print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def buy(times):
    # 标志位，在点击“结算”按钮后不再进入 while flag 循环
    flag = 1
    while flag:
        # 记录当前时间，使用datatime内置模块
        now2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(times)
        print(now2)
        # 对比时间，时间到的话就点击结算
        if now2 >= times:
            if driver.find_element(By.ID, 'J_Go'):
                driver.find_element(By.ID, 'J_Go').click()
                flag = 0

        while flag == 0:
            try:
                driver.find_element(By.XPATH, '//*[@id="submitOrderPC_1"]/div/a[2]').click()
                print('抢购成功，请尽快付款')

            except:
                # 实测只点击一次“结算”按钮可能点不上，所以flag重置1反复点
                flag = 1
                print('正在再次尝试提交订单')

        # print(now2)
        time.sleep(0.1)


if __name__ == "__main__":
    buy_times = input("请输入抢购时间(例如格式：2022-08-17 21:00:00):")
    buy(buy_times)