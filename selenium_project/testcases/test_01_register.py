import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_project.data.data_process import DataProcess
from selenium_project.data.data_read import DataRead


class TestCase:
    __driver = None  # 类变量，用于存储webdriver实例
    dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    xls_path = os.path.join(dir_path, 'selenium_test.xls')

    def setup_class(self):
        # 每次执行测试前初始化webdriver，并最大化窗口
        options = webdriver.ChromeOptions()
        # 使用无头浏览器运行用例
        options.add_argument('--headless')
        options.add_argument('--start-maximized')
        self.__driver = webdriver.Chrome(options)
        self.__driver.maximize_window()

    def teardown_class(self):
        # 每次执行测试后关闭webdriver
        self.__driver.quit()

    # 使用pytest.mark.parametrize装饰器，参数化测试数据
    @allure.story('测试注册')
    @pytest.mark.parametrize('data', DataRead.data_read(xls_path, 'register'))
    def test_register(self, data):
        # 如果数据标记为跳过，则使用pytest.skip跳过测试
        if data.is_skip:
            pytest.skip("Data is marked to be skipped")

        # 打开注册页面
        self.__driver.get(data.url)

        # 对数据进行处理
        data = DataProcess.data_process(data, self.__driver)

        # 获取输入的用户名、密码、确认密码、邮箱和验证码
        username_str = data.get_parameters_value('username')
        pwd_str = data.get_parameters_value('pwd')
        confirmPwd_str = data.get_parameters_value('confirmPwd')
        email_str = data.get_parameters_value('email')
        captcha_str = data.get_parameters_value('captcha_str')
        expect = data.expect  # 预期结果

        # 输入用户名
        username = self.__driver.find_element(By.NAME, value='username')
        username.send_keys(username_str)

        # 输入邮箱
        email = self.__driver.find_element(By.NAME, 'email')
        email.send_keys(email_str)

        # 输入密码
        password = self.__driver.find_element(By.NAME, value='pwd')
        password.send_keys(pwd_str)

        # 输入确认密码
        confirm_pwd = self.__driver.find_element(By.NAME, value='confirmPwd')
        confirm_pwd.send_keys(confirmPwd_str)

        # 输入验证码
        captcha_input_box = self.__driver.find_element(value='captcha')
        captcha_input_box.send_keys(captcha_str)

        # 点击注册按钮
        register_button = self.__driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[6]/div/button')
        register_button.click()

        # 等待弹窗出现
        WebDriverWait(self.__driver, 5).until(EC.alert_is_present())

        # 切换到弹窗，获取弹窗文本
        alert = self.__driver.switch_to.alert
        alert_text = alert.text
        alert.accept()

        # 断言弹窗文本与预期结果一致
        assert alert_text == expect
