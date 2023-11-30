from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


# http://sahitest.com/demo/ 测试网站，方便测试元素
class WebElementTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        self.element = self.driver.find_element(value='t1')
        print(f'打印对象的type：{type(self.element)}')  # 可以用type()打印一个对象的类型
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
        # 输入内容，可以输入字符串，也可以输入类似 Keys.ENTER，执行回车操作
        self.element.send_keys('selenium')
        sleep(2)

        # 单击
        self.element.click()
        sleep(2)

        # 获取元素的 type 属性
        print(f'获取元素的 type 属性：{self.element.get_attribute("type")}')

        # 获取元素的 value 属性
        print(f'获取元素的 value 属性：{self.element.get_attribute("value")}')
        sleep(2)

        # 清空内容
        self.element.clear()
        sleep(2)

        # 是否被选中
        print(f'是否被选中：{self.element.is_selected()}')

        # 是否可用
        print(f'是否可用：{self.element.is_enabled()}')

        # 是否显示
        print(f'是否显示：{self.element.is_displayed()}')

        # 获取元素的 css 属性中的 font 字体
        print(f'获取元素的 css 属性中的 font 字体：{self.element.value_of_css_property("font")}')

        # 获取元素的 css 属性中的 color 颜色
        print(f'获取元素的 css 属性中的 color 颜色：{self.element.value_of_css_property("color")}')

    def test_findelement_from_element(self):
        # 也可以通过元素来定位元素里面的元素
        element1 = self.driver.find_element(By.XPATH, '/html/body')  # 这是整个页面
        element2 = element1.find_element(value='t1')  # 在xpath="/html/body"的元素中找到id = "t1"的元素
        element2.send_keys('selenium')
        sleep(2)


if __name__ == '__main__':
    driver = WebElementTest()
    driver.test_webelement_property()
    driver.test_webelement_method()
    driver.test_findelement_from_element()
