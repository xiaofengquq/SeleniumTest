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


def test1():
    print("test1 run")
    import subprocess
    p = subprocess.Popen(r"C:\Program Files\selenium_driver\chromedriver.exe")
    sleep(1)
    p.terminate()
    p.communicate()


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
    test1()
    testcase = TestCase()
    testcase.baiduTest()
    googleTest()
