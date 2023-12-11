from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# *代表任意多个参数
def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e


if __name__ == '__main__':
    webdriver = webdriver.Chrome()
    webdriver.get('https://www.google.com')
    get_element(webdriver, By.ID, 'APjFqb').send_keys('selenium')
    sleep(1)
    # get_element(driver, *loc)中的*loc同样可以像下面这样传递
    # 定义元组需要将参数用括号括起来
    loc = (By.PARTIAL_LINK_TEXT, '隐私')
    # 如果变量是一个元组，那么传递这个元组的时候，同样需要在变量名前面加 *号（这被称为“解包”）
    # 这种方式的作用是将元组的元素分别传递给函数，而不是将整个元组作为一个参数传递。
    get_element(webdriver, *loc).click()
