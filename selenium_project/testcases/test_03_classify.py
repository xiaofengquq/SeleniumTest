import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_project.util.util import Util


class TestClassify(unittest.TestCase):
    @staticmethod
    def test_Classify():
        driver = webdriver.Chrome()
        driver.get('http://localhost:8080/jpress/admin/login')
        driver.maximize_window()
        Util.login(driver, 'admin', '915366', True)
        sleep(2)
