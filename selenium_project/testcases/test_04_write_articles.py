import time
import traceback
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_project.util.util import Util


class TestWriteArticles(unittest.TestCase):

    @staticmethod
    def test_write_articles():
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
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[href="/jpress/admin/article/write"]'), '写文章'),
                'Element not found')
            print('ok')
        except:
            # 捕获异常并打印堆栈信息
            traceback.print_exc()
        # 点击'写文章'，进入写文章页面
        driver.find_element(By.CSS_SELECTOR, 'a[href="/jpress/admin/article/write"]').click()
        # 定位文章标题输入框，并输入当前时间的字符串格式作为标题
        title = driver.find_element(value='article-title')  # 定位文章标题输入框
        title.send_keys('标题' + time.strftime('%Y年%m月%d日 %H-%M-%S'))  # 输入标题，格式为“标题+年月日时分秒”
        # 定位页面的iframe元素，并切换到该iframe
        iframe = driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')  # 定位iframe
        driver.switch_to.frame(iframe)  # 切换到iframe
        # 在iframe中找到可编辑的输入框，并输入特定的文本
        input_box = driver.find_element(By.CSS_SELECTOR,
                                        '.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders')  # 定位输入框
        input_box.send_keys('915366')  # 输入文本“915366”
        # 切换回默认的content，以便能够点击提交按钮
        driver.switch_to.default_content()
        # 点击提交按钮，提交文章
        driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-sm.submitBtn').click()
        sleep(2)
