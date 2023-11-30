import traceback
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait


# 测试 selenium显式等待（WebDriverWait）

class FormTest05(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com')

    def test_sleep(self):
        # sleep()只用在调试中
        search = self.driver.find_element(value='APjFqb')
        search.send_keys('selenium')
        sleep(2)  # 线程阻塞 blocking
        search.send_keys(Keys.ENTER)
        sleep(2)
        self.driver.quit()

    def test_implicitly(self):
        # 隐式等待，设置等待时间为 5 秒，对整个 WebDriver 对象生效，一旦设置后，将在查找元素时等待指定的时间
        self.driver.implicitly_wait(5.0)

        # 查找具有 'APjFqb' 属性值的元素，如果元素未立即找到，将等待最多 5 秒
        search = self.driver.find_element(value='APjFqb')
        search.send_keys('selenium')
        sleep(2)  # 线程阻塞 blocking
        search.send_keys(Keys.ENTER)
        sleep(2)
        self.driver.quit()

    @staticmethod
    def check_element_present(driver):
        try:
            driver.find_element(value='123')
            return True
        except NoSuchElementException:
            # 如果找不到元素或发生异常，则返回 False
            return False

    def test_webdriver_wait(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            result = wait.until(self.check_element_present, message='Element not found')
            print(f'Element found: {result}')
        except:
            traceback.print_exc()


if __name__ == '__main__':
    form_test = FormTest05()
    # form_test.test_sleep()
    # form_test.test_implicitly()
    form_test.test_webdriver_wait()
