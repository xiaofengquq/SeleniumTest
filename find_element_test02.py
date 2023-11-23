from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestCase:
    def test_id(self):
        #   同一个页面的id肯定是唯一的，所以一般的定位会使用id
        print('test_id run')
        driver = webdriver.Chrome()
        sleep(1)
        driver.get('http://www.google.com')
        driver.maximize_window()
        # def find_element(self, by=By.ID, value: Optional[str] = None) -> WebElement:
        # 如果没有传递by的话，默认是By.ID
        search = driver.find_element(By.ID, 'APjFqb')
        # search = driver.find_element(value='APjFqb') 也可以写成这样
        search.send_keys('selenium')
        sleep(1)
        search.send_keys(Keys.ENTER)
        sleep(3)
        driver.quit()

    def test_XPath(self):
        # Chrome浏览器可以右键元素 -> 检查，然后右键，copy -> copy XPath来获取元素的XPath
        print('test_XPath run')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        sleep(1)
        search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        search.send_keys('selenium')
        search.send_keys(Keys.ENTER)
        sleep(3)
        driver.quit()

    def test_link_text(self):
        #   用超链文字检索元素
        print('test_link_text run')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        sleep(1)
        search = driver.find_element(By.LINK_TEXT, '隐私权')
        search.click()
        sleep(3)
        driver.quit()

    def test_partial_link_text(self):
        #   用部分超链文字检索元素
        print('test_partial_link_text run')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        sleep(1)
        search = driver.find_element(By.PARTIAL_LINK_TEXT, '隐私')
        search.click()
        sleep(3)
        driver.quit()

    def test_name(self):
        #   由于用一个name可能对应多个元素，find_element(By.NAME, 'q')并不会全部返回，仅会返回第一个
        #   如果想全部获取到，需要使用 find_elements(By.NAME, 'q') 这个方法会返回一个 List[WebElement]
        print('test_name run')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        sleep(1)
        search = driver.find_element(By.NAME, 'q')
        search.send_keys('selenium')
        search.send_keys(Keys.ENTER)
        sleep(3)
        driver.quit()

    def test_tag(self):
        #   find_element(By.TAG_NAME, 'textarea') 这个方法一般很少用，因为tag并不能保证准确定位到元素
        print('test_tag run')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        sleep(1)
        search = driver.find_element(By.TAG_NAME, 'textarea')
        search.send_keys('selenium')
        search.send_keys(Keys.ENTER)
        sleep(3)
        driver.quit()

    def test_class(self):
        # 通过class name来定位
        print('test_class run')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        sleep(1)
        search = driver.find_element(By.CLASS_NAME, 'gLFyf')
        search.send_keys('selenium')
        search.send_keys(Keys.ENTER)
        sleep(3)
        driver.quit()

    def test_css_selector(self):
        #   使用css选择器定位元素
        #   同样的，Chrome浏览器可以右键元素 -> 检查，然后右键，copy -> copy selector来获取元素的CSS_SELECTOR
        print('test_css_selector run')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.maximize_window()
        sleep(1)
        search = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
        search.send_keys('selenium')
        search.send_keys(Keys.ENTER)
        sleep(3)
        driver.quit()


if __name__ == '__main__':
    testcase = TestCase()

    # testcase.test_id()
    testcase.test_XPath()
    # testcase.test_link_text()
    # testcase.test_partial_link_text()
    # testcase.test_name()
    # testcase.test_tag()
    # testcase.test_class()
    # testcase.test_css_selector()
