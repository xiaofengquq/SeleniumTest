import os.path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# 测试 表单复选，单选

class FormTest02(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        dir_path = os.path.dirname(os.path.abspath(__file__))
        self.path = 'file:///' + os.path.join(dir_path, 'forms_test.html')
        self.driver.get(self.path)

    def test_checkbox(self):
        swimming_checkbox = self.driver.find_element(By.NAME, 'swimming')
        # 如果checkbox没有被选中，则单击将其选中
        if not swimming_checkbox.is_selected():
            swimming_checkbox.click()
        sleep(1)
        reading_checkbox = self.driver.find_element(By.NAME, 'reading')
        if not reading_checkbox.is_selected():
            reading_checkbox.click()
        sleep(1)

    def test_radio_button(self):
        gender_list = self.driver.find_elements(By.NAME, 'gender')
        for gender in gender_list:
            gender.click()
            sleep(1)


if __name__ == '__main__':
    form_test = FormTest02()
    form_test.test_checkbox()
    form_test.test_radio_button()
    sleep(1)
