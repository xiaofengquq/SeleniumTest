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
        title = driver.find_element(value='article-title')
        title.send_keys('标题' + time.strftime('%Y年%m月%d日 %H-%M-%S'))
        iframe = driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        driver.switch_to.frame(iframe)
        input_box = driver.find_element(By.CSS_SELECTOR,
                                        '.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders')
        input_box.send_keys('915366')
        driver.switch_to.default_content()
        driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-sm.submitBtn').click()
        sleep(2)
