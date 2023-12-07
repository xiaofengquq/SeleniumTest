from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys


class ExecuteScriptTest01:
    def __init__(self):
        # 初始化Chrome浏览器
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')

    def test_alert(self):
        # 执行JavaScript弹窗脚本，弹出alert框
        self.driver.execute_script("alert('test')")
        sleep(2)
        # 切换到alert并接受
        self.driver.switch_to.alert.accept()

    def return_title(self):
        # 执行JavaScript脚本获取页面标题并打印
        js = 'return document.title'
        print(self.driver.execute_script(js))

    def change_style(self):
        # 执行JavaScript脚本修改页面元素样式
        js = 'var q = document.getElementById("APjFqb"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(2)

    def scroll(self):
        # 执行JavaScript脚本滚动页面至底部
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        search = self.driver.find_element(value='APjFqb')
        search.send_keys('selenium')
        search.send_keys(Keys.ENTER)
        # 执行滚动脚本
        self.driver.execute_script(js)
        sleep(2)


if __name__ == '__main__':
    es_test = ExecuteScriptTest01()
    # 分别测试注释掉的方法
    # es_test.test_alert()
    # es_test.return_title()
    # es_test.change_style()
    es_test.scroll()
