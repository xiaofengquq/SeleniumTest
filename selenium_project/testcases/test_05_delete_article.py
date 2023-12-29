import traceback
import unittest
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains as AC
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
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a[href="/jpress/admin/article"]'), '文章管理'),
                'Element not found')
            print('ok')
        except NoSuchElementException as e:
            # 捕获异常并打印堆栈信息
            traceback.print_exc()
        # 点击'文章管理'，进入 文章管理 页面
        driver.find_element(By.CSS_SELECTOR, 'a[href="/jpress/admin/article"]').click()
        # 使用CSS选择器中的 伪类，定位到第二个文章（table table-striped下面有3个tr标签）的strong标签
        article = driver.find_element(By.CSS_SELECTOR, '.table.table-striped tr:nth-child(3) strong')
        ac = AC(driver)
        ac.move_to_element(article).perform()
        print(f'{article.get_attribute("innerHTML")}')
        sleep(1)
        # 找到‘垃圾箱’按钮并点击删除文章
        delete = driver.find_element(By.CSS_SELECTOR,
                                     '.box-body > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > '
                                     '.jp-actionitem > a:nth-child(3)')
        print(f'{delete.get_attribute("innerHTML")}')
        ac.move_to_element(delete).click().perform()

        sleep(2)
