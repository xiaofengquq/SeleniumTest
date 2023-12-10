import os.path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 测试 弹窗

class FormTest04(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        self.driver.get('file:///' + os.path.join(path, 'forms_test.html'))

    def test_alert(self):
        self.driver.find_element(By.ID, 'alert').click()
        # 三种弹窗对于webdriver来说都是alert属性
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(2)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element(value='confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(2)
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element(value='prompt').click()
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        prompt.send_keys('123')
        sleep(2)
        prompt.dismiss()
        # 关闭弹窗后需要重新获取弹窗元素
        self.driver.find_element(value='prompt').click()
        prompt = self.driver.switch_to.alert
        prompt.send_keys('456')
        sleep(2)
        prompt.accept()
        sleep(2)


if __name__ == '__main__':
    form_test = FormTest04()
    # No2_form.test_alert()
    # No2_form.test_confirm()
    form_test.test_prompt()
