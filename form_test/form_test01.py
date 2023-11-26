import os
from time import sleep

from selenium import webdriver


# 测试 表单短文本、密码及提交

class FormTest01(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_test(self):
        # __file__ 返回包含当前脚本的绝对路径的字符串
        # os.path.abspath(__file__) 拿到的是当前文件的路径
        # 将当前文件路径当做参数传递到os.path.dirname()里，就能拿到文件所属目录的路径了
        path = os.path.dirname(os.path.abspath(__file__))
        # 本地路径协议：file:/// 再加上刚才获取到的目录路径及html的文件名
        # 即可以获得html文件的绝对路径
        # 使用os.path.join()来拼接，可以保证兼容所有操作系统
        file_path = 'file:///' + os.path.join(path, 'forms_test.html')
        print(file_path)
        # 之后的操作和之前就一样了，只需要把get中的url换成本地html的路径即可
        self.driver.get(file_path)

        # 找到用户名输入框并输入用户名
        username_input = self.driver.find_element(value='username')
        username_input.send_keys("admin")
        sleep(1)

        # 找到密码输入框并输入密码
        password_input = self.driver.find_element(value='pwd')
        password_input.send_keys("123")
        sleep(1)

        # 找到提交按钮并点击
        submit_button = self.driver.find_element(value='submit')
        submit_button.click()
        sleep(1)
        # 切换到弹窗并接受弹窗
        # 不能在页面上存在弹窗的时候操作后面的元素，比如下面的清空用户名和密码输入框，否则会报错
        self.driver.switch_to.alert.accept()
        sleep(1)

        # 清空用户名和密码输入框
        username_input.clear()
        sleep(1)
        password_input.clear()
        sleep(1)

        self.driver.quit()


if __name__ == '__main__':
    form_test = FormTest01()
    form_test.login_test()
    sleep(3)
