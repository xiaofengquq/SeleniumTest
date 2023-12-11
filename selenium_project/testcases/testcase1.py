import traceback
from time import sleep

import pyautogui
from selenium import webdriver


def test():
    print('test1')


def JPress_test():
    driver = webdriver.Chrome()
    driver.get('https://www.jpress.cn/user/register')
    # 在非最大化窗口下，使用rect坐标可能会出现偏移
    driver.maximize_window()
    check_box = driver.find_element(value='agree')
    # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted
    # 有些元素无法通过selenium直接操作
    try:
        check_box.click()
    except Exception as e:
        # traceback.print_exc()
        print(e)
    # webelement里的rect是一个 包含元素大小和位置的字典。
    # rect里的坐标，是一个元素的左顶点坐标，需要向右移一点，向下移一点
    rect = check_box.rect
    pyautogui.click(rect['x'] + 10, rect['y'] + 130)
    sleep(3)
