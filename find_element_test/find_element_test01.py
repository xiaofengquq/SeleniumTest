from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        print("TestCase run")
        self.driver = webdriver.Chrome()

    def baiduTest(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        sleep(1)
        self.driver.find_element(By.ID, "su").click()
        sleep(3)
        self.driver.quit()


def googleTest():
    print("test2 run")
    driver = webdriver.Chrome()
    sleep(1)
    driver.get("http://www.google.com")
    search = driver.find_element(By.ID, "APjFqb")
    search.send_keys("selenium")
    sleep(1)
    search.send_keys(Keys.ENTER)
    sleep(3)
    driver.quit()


if __name__ == '__main__':
    testcase = TestCase()
    testcase.baiduTest()
    googleTest()
