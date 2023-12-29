import traceback
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium_project.util.util import Util


class TestClassify(unittest.TestCase):
    @staticmethod
    def test_Classify():
        # 初始化Chrome浏览器
        driver = webdriver.Chrome()
        # 打开测试页面
        driver.get('http://localhost:8080/jpress/admin/login')
        # 最大化浏览器窗口
        driver.maximize_window()
        # 使用Util模块的login方法进行登录
        Util.login(driver, 'admin', '915366', True)
        # 点击左侧菜单的'文章'
        driver.find_element(By.CSS_SELECTOR, 'li.treeview').click()
        # 创建WebDriverWait对象，设置最长等待时间为3秒
        wait = WebDriverWait(driver, 3)
        # 等待'分类'出现，如果3秒内未出现，则抛出异常
        try:
            wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[href="/jpress/admin/article/category"]'), '分类'),
                'Element not found')
            print('ok')
        except:
            # 捕获异常并打印堆栈信息
            traceback.print_exc()
        # 点击'分类'，进入分类页面
        driver.find_element(By.CSS_SELECTOR, 'a[href="/jpress/admin/article/category"]').click()
        # 查找分类名称输入框
        name = driver.find_element(By.CSS_SELECTOR, 'div.col-sm-9 input[class="form-control"]')
        # 输入分类名称
        name.send_keys('')
        # 查找父分类选择框
        parent = driver.find_element(By.NAME, 'category.pid')
        # 创建Select对象，以便选择下拉框中的选项
        se = Select(parent)
        # 打印Select对象中的选项，以便调试
        print(se)
        # 通过可见文本选择下拉框中的'python'选项
        se.select_by_visible_text('python')
        # 查找分类slug输入框
        slug = driver.find_element(By.CSS_SELECTOR, 'div.col-sm-9 input[name="category.slug"]')
        # 输入分类slug
        slug.send_keys('python')
        # 查找提交按钮
        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
        # 点击提交按钮，创建分类
        submit_button.click()
        sleep(2)
