import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_project.data.data_process import DataProcess
from selenium_project.data.data_read import DataRead


class TestCase(unittest.TestCase):
    __driver = None
    data_list = []

    @classmethod
    def setUpClass(cls):
        cls.__driver = webdriver.Chrome()
        cls.__driver.maximize_window()
        cls.data_list = DataRead.data_read('register')

    @classmethod
    def tearDownClass(cls):
        cls.__driver.quit()

    # @unittest.skipIf(data)
    @unittest.parametrize('test_input', get_test_data())
    def test_register(self, data):
        self.__driver.get(data.url)
        data = DataProcess.data_process(data, self.__driver)
        username_str = data.get_parameters_value('username')
        pwd_str = data.get_parameters_value('pwd')
        confirmPwd_str = data.get_parameters_value('confirmPwd')
        email_str = data.get_parameters_value('email')
        captcha_str = data.get_parameters_value('captcha_str')
        expect = data.expect

        username = self.__driver.find_element(By.NAME, value='username')
        username.send_keys(username_str)

        email = self.__driver.find_element(By.NAME, 'email')
        email.send_keys(email_str)

        password = self.__driver.find_element(By.NAME, value='pwd')
        password.send_keys(pwd_str)

        confirm_pwd = self.__driver.find_element(By.NAME, value='confirmPwd')
        confirm_pwd.send_keys(confirmPwd_str)

        captcha_input_box = self.__driver.find_element(value='captcha')
        captcha_input_box.send_keys(captcha_str)

        register_button = self.__driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[6]/div/button')
        register_button.click()

        WebDriverWait(self.__driver, 5).until(EC.alert_is_present())
        alert = self.__driver.switch_to.alert

        self.assertEqual(alert.text, expect,
                         '断言结果与预期不符' + '\n' '断言结果：'f'{alert.text}' + '\n' f'预期：{expect}')
        sleep(1)
        alert.accept()
