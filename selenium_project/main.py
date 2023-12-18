# 从时间模块导入 sleep 函数
from time import sleep

# 导入 Selenium WebDriver 和相关模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_project.util.util import Util

if __name__ == '__main__':
    # 创建 Chrome WebDriver 实例
    driver = webdriver.Chrome()
    # 打开登录页
    driver.get('http://localhost:8080/jpress/user/login')

    # 获取登录页面的验证码图片并转换为二进制数据
    image_byte = Util.take_qr_code(driver, 'captcha-img')

    # 使用 OCR 工具识别验证码图片内容
    captcha_string = Util.captcha_to_string(image_byte)

    # 定位用户名输入框并输入用户名
    user = driver.find_element(By.NAME, 'user')
    user.send_keys('admin')

    # 定位密码输入框并输入密码
    password = driver.find_element(By.NAME, 'pwd')
    password.send_keys('915366')

    # 定位验证码输入框并输入验证码内容
    captcha = driver.find_element(By.NAME, 'captcha')
    captcha.send_keys(captcha_string)

    # 等待3秒
    sleep(3)

    # 定位登录按钮并点击
    login_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/form/div[4]/div/button')
    login_button.click()

    # 等待3秒
    sleep(3)
