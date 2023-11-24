from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# http://sahitest.com/demo/ 测试网站，方便测试元素
class WebElementTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        self.element = self.driver.find_element(value='t1')
        print(type(self.element))  # 可以用type()打印一个对象的类型
        # <class 'selenium.webdriver.remote.webelement.WebElement'>
        # 说明 self.element 的类型是 WebElement
        # 想要快速找到 WebElement 这个类，可以这样写，然后alt + enter导入，在点击左侧的结构即可看到类的架构
        e1 = WebElement
        # 结构中，P代表property，属性
        # m代表method，方法

    def test_webelement_property(self):
        print(f'id：{self.element.id}')  # 唯一标识
        print(f'标签名称：{self.element.tag_name}')
        print(f'宽高：{self.element.size}')
        print(f'宽高和坐标：{self.element.rect}')
        print(f'文本内容：{self.element.text}')

    def test_webelement_method(self):
        self.element.send_keys('selenium')  # 输入内容，可以输入字符串，也可以输入类似Keys.ENTER，执行回车操作
        sleep(2)
        self.element.click()  # 单击
        sleep(2)

        # 这里get_attribute("type")中的字符串如果使用 单引号''，会报错，
        # 因为 f-string 中的花括号 {} 内的表达式被误解为字符串的一部分，需要使用 双引号""
        print(f'获取元素的type属性：{self.element.get_attribute("type")}')
        print(f'获取元素的value属性：{self.element.get_attribute("value")}')
        sleep(2)
        self.element.clear()  # 清空内容
        sleep(2)
        # self.element.is_selected()  # 是否被选中
        # self.element.is_enabled()  # 是否可用
        # self.element.is_displayed()  # 是否显示
        print(f'获取元素的css属性中的font字体：{self.element.value_of_css_property("font")}')
        print(f'获取元素的css属性中的color颜色：{self.element.value_of_css_property("color")}')

    def test_findelement_from_element(self):
        # 也可以通过元素来定位元素里面的元素
        element1 = self.driver.find_element(By.XPATH, '/html/body')  # 这是整个页面
        element2 = element1.find_element(value='t1')  # 在xpath="/html/body"的元素中找到id = "t1"的元素
        element2.send_keys('selenium')
        sleep(2)


if __name__ == '__main__':
    driver = WebElementTest()
    # driver.test_webelement_property()
    # driver.test_webelement_method()
    driver.test_findelement_from_element()
