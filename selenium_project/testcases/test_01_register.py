import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_project.util.util import Util


class TestCase(unittest.TestCase):
    __driver = None

    @classmethod
    def setUpClass(cls):
        cls.__driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.__driver.quit()

    def test_register(self):
        self.__driver.get('http://localhost:8080/jpress/user/register')
        username = self.__driver.find_element(By.NAME, value='username')
        username.send_keys('yzw')

        password = self.__driver.find_element(By.NAME, value='pwd')
        password.send_keys('915366')

        captcha = self.__driver.find_element(value='captcha')
        captcha_string = Util.take_qr_code_string(self.__driver, 'captchaimg')
        print(captcha_string)
        captcha.send_keys(captcha_string)

        register_button = self.__driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[6]/div/button')
        register_button.click()

        sleep(3)
