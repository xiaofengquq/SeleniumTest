import os.path
import traceback
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 测试 selenium 显式等待（WebDriverWait）

class FormTest05(object):
    def __init__(self):
        # 初始化 WebDriver 对象
        self.driver = webdriver.Chrome()
        # 打开 Google 页面
        self.driver.get('https://www.google.com')

    def test_sleep(self):
        print('test_sleep run')
        # sleep() 只用在调试中
        # 查找具有 'APjFqb' 属性值的元素
        search = self.driver.find_element(value='APjFqb')
        # 在搜索框中输入 'selenium'
        search.send_keys('selenium')
        # 线程阻塞
        sleep(2)
        # 在搜索框中按下回车键
        search.send_keys(Keys.ENTER)
        sleep(2)
        # 关闭浏览器
        self.driver.quit()

    def test_implicitly(self):
        print('test_implicitly run')
        # 隐式等待，设置等待时间为 5 秒，对整个 WebDriver 对象生效，
        # 一旦设置后，将在查找元素时等待指定的时间
        self.driver.implicitly_wait(5.0)

        # 查找具有 'APjFqb' 属性值的元素，如果元素未立即找到，将等待最多 5 秒
        search = self.driver.find_element(value='APjFqb')
        # 在搜索框中输入 'selenium'
        search.send_keys('selenium')
        sleep(2)
        # 在搜索框中按下回车键
        search.send_keys(Keys.ENTER)
        sleep(2)
        # 关闭浏览器
        self.driver.quit()

    def test_webdriver_wait(self):
        print('test_webdriver_wait run')
        # 创建 WebDriverWait 对象，设置最大等待时间为 5 秒
        wait = WebDriverWait(self.driver, 5)
        try:
            # 等待标题为 'Google'，如果等待超时，抛出 TimeoutException 异常
            wait.until(EC.title_is('Google'), message='Element not found')
            # 查找具有 'APjFqb' 属性值的元素
            search = self.driver.find_element(value='APjFqb')
            # 在搜索框中输入 'selenium'
            search.send_keys('selenium')
            # 在搜索框中按下回车键
            search.send_keys(Keys.ENTER)
            sleep(3)
        except:
            # 捕获异常并打印堆栈信息
            traceback.print_exc()


if __name__ == '__main__':
    # 创建 FormTest05 实例
    form_test = FormTest05()
    # 调用测试方法
    # No2_form.test_sleep()
    # No2_form.test_implicitly()
    form_test.test_webdriver_wait()
