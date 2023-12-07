from time import sleep, strftime, localtime, time

from selenium import webdriver
from selenium.webdriver import Keys


class ScreenShotTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def screenshot(self):
        search = self.driver.find_element(value='kw')
        search.send_keys('selenium')
        search.send_keys(Keys.ENTER)
        sleep(2)

        # 会在当前文件夹下生成一张名为google.png的截图
        # self.driver.save_screenshot('google.png')

        # 将时间格式化
        # Windows文件命名不能使用冒号 :
        st = strftime('%Y年%m月%d日 %H-%M-%S', localtime(time()))
        file_name = st + '.png'
        self.driver.save_screenshot(file_name)


if __name__ == '__main__':
    screenshot_test = ScreenShotTest()
    screenshot_test.screenshot()
