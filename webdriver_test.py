from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class WebDriverTest(object):
    # 如果不写self，方法写成
    # driver = webdriver.Chrome()
    # driver.get('https://www.google.com')，那么这个driver就是一个局部变量
    # 在其他类的方法中就无法使用这个变量了
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')
        self.driver.maximize_window()

    def test_property(self):
        print(f'浏览器名称：{self.driver.name}')
        print(f'URL：{self.driver.current_url}')
        print(f'title：{self.driver.title}')  # 当前浏览器窗口的标题

        # f-string（格式化字符串字面值）的一种字符串格式化方法，是 Python 3.6 及更高版本引入的功能
        # 它允许在字符串中嵌入表达式，而无需调用 format 方法。
        # 快捷生成f-string的方法，在需要的地方输入{}，输入表达式联想后回车即可
        print(f'句柄：{self.driver.window_handles}')  # 句柄，在浏览器中，每个打开的标签页或窗口都有一个 唯一 的标识符，称为窗口句柄
        # 可以通过句柄来定位窗口

        print(f'页面源码：{self.driver.page_source}')
        self.driver.quit()

    def test_method(self):
        element = self.driver.find_element(By.ID, 'APjFqb')  # find_element()方法，用于定位元素
        element.send_keys('selenium')
        element.send_keys(Keys.ENTER)
        sleep(1)
        self.driver.back()  # back()方法，返回上一页
        sleep(1)
        self.driver.refresh()  # refresh()方法，刷新当前页面
        sleep(1)
        self.driver.forward()  # forward()方法，前进到下一页
        sleep(1)

        self.driver.close()  # close()方法，关闭当前tab
        self.driver.quit()  # quit()方法，关闭浏览器


if __name__ == '__main__':
    driver = WebDriverTest()
    # driver.test_property()
    driver.test_method()
