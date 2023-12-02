from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains as AC, Keys
from selenium.webdriver.common.by import By


class FormTest08:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')
        self.ac = AC(self.driver)

    def test_keyboard_input(self):
        searchBox = self.driver.find_element(By.ID, 'APjFqb')
        searchBox.send_keys('selenium')
        sleep(1)
        # 模拟Ctrl + A
        searchBox.send_keys(Keys.CONTROL, 'A')
        sleep(1)
        # 模拟Ctrl + X
        searchBox.send_keys(Keys.CONTROL, 'X')
        sleep(1)
        # 模拟Ctrl + V
        searchBox.send_keys(Keys.CONTROL, 'V')
        sleep(1)


if __name__ == '__main__':
    form_test = FormTest08()
    form_test.test_keyboard_input()

