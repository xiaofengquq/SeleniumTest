import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        username_str = Util.get_random_str(8)
        pwd_str = '915366'
        confirmPwd_str = '915366'
        email_str = Util.get_random_str(11) + '@gmail.com'
        expect = '注册成功，点击确定进行登录。'

        self.__driver.get('http://localhost:8080/jpress/user/register')
        username = self.__driver.find_element(By.NAME, value='username')
        username.send_keys(username_str)

        email = self.__driver.find_element(By.NAME, 'email')
        email.send_keys(email_str)

        password = self.__driver.find_element(By.NAME, value='pwd')
        password.send_keys(pwd_str)

        confirmPwd = self.__driver.find_element(By.NAME, value='confirmPwd')
        confirmPwd.send_keys(confirmPwd_str)

        captcha = self.__driver.find_element(value='captcha')
        captcha_string = Util.get_qr_code_string(self.__driver, 'captchaimg')
        captcha.send_keys(captcha_string)

        register_button = self.__driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[6]/div/button')
        register_button.click()

        WebDriverWait(self.__driver, 5).until(EC.alert_is_present())
        alert = self.__driver.switch_to.alert

        assert alert.text == expect, (
                '断言结果与预期不符' + '\n' '断言结果：'f'{alert.text}' + '\n' f'预期：{expect}')
        sleep(3)
        alert.accept()
