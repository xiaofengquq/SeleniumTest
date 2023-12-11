# 打开百度首页-新闻，然后在首页和新闻两个标签页之间切换
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # 创建 Chrome WebDriver 实例
    driver = webdriver.Chrome()

    # 打开百度首页
    driver.get('https://www.baidu.com')

    # 窗口最大化
    driver.maximize_window()

    # 定位百度首页上的“新闻”链接并点击
    element = driver.find_element(By.LINK_TEXT, "新闻")
    element.click()

    # 获取所有窗口的句柄
    windows = driver.window_handles

    # 循环两次，切换两个标签页
    for i in range(2):
        for window in windows:
            # 切换到指定窗口
            driver.switch_to.window(window)
            sleep(1)
