from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    chrome_options = Options()
    # 添加调试器地址，以便在已经通过SSO验证的浏览器中访问后台
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # 使用配置好的chrome_options初始化WebDriver
    driver = webdriver.Chrome(chrome_options)
    # 最大化浏览器窗口
    driver.maximize_window()
    # 打开后台
    driver.get('https://smsop.sys.wanmei.net/')
    # 点击一级菜单
    level_1_menu = driver.find_element(By.XPATH, '/html/body/section/div[1]/div[3]/ul/li[2]/a/span')
    level_1_menu.click()
    # 点击二级菜单
    level_2_menu = driver.find_element(By.XPATH, '/html/body/section/div[1]/div[3]/ul/li[2]/ul/li[1]/a')
    level_2_menu.click()
    # 切换到指定 iframe 中，以便于后续操作
    driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/section/div[2]/div[2]/iframe[2]'))
    # 将页面向右拖动200个像素，以显示右侧按钮
    AC = ActionChains(driver)
    AC.move_by_offset(1690, 402).click_and_hold().move_by_offset(200, 0).perform()
    # 使用 CSS 选择器找到td标签下，所有具有 'btn btn-default' 类名的按钮
    # 这里使用空格或者大于号都找到
    buttons = driver.find_elements(By.CSS_SELECTOR, 'td>.btn.btn-default')

    # 对找到的第一个按钮执行点击操作
    buttons[0].click()
