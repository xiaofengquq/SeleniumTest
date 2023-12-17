from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains as AC


def JPress_test():
    driver = webdriver.Chrome()
    driver.get('https://www.jpress.cn/user/register')
    # 在非最大化窗口下，使用rect坐标可能会出现偏移
    driver.maximize_window()
    check_box = driver.find_element(value='agree')
    try:
        check_box.click()
    except Exception as e:
        # Message: element click intercepted: Element <input type="checkbox"
        # class="custom-control-input" id="agree"> is not clickable at point (856, 576). Other element would receive
        # the click:
        print(e)
    # 有些元素无法通过webelement直接操作，需要通过ActionChains
    ac = AC(driver)
    ac.move_to_element(check_box).click().perform()
    sleep(3)


if __name__ == '__main__':
    JPress_test()
