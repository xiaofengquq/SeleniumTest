import traceback
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.by import By


# FrameTest类用于测试在HTML中的frame操作
# HTML中的frame就是用来加载和显示web内容的矩形区域。

class FrameTest:
    def __init__(self):
        # 初始化Chrome浏览器驱动并打开测试网页
        self.driver = webdriver.Chrome()
        # 这个页面包含一个frame
        self.driver.get('https://sahitest.com/demo/framesTest.htm')
        self.ac = AC(self.driver)

    def test(self):
        # 尝试在主页面中查找并点击一个元素，如果元素在frame中，这将抛出异常
        e1 = self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]')
        e1.click()
        sleep(5)

    def switch_to_frame(self):
        # 定位到名为 top 的frame并切换
        first_frame = self.driver.find_element(By.NAME, 'top')
        self.driver.switch_to.frame(first_frame)
        # 在 top frame中操作元素
        e1 = self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]')
        e1.click()
        sleep(3)
        # 切换回主页面
        self.driver.switch_to.default_content()
        # 定位到第二个frame并切换
        second_frame = self.driver.find_element(By.XPATH, '/html/frameset/No7_frame[2]')
        self.driver.switch_to.frame(second_frame)
        # 在第二个frame中操作元素
        e2 = self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[3]')
        e2.click()
        sleep(3)


if __name__ == '__main__':
    frame_test = FrameTest()
    try:
        # 尝试在主页面中操作元素
        frame_test.test()
    except:
        # 如果抛出异常，打印异常堆栈信息
        traceback.print_exc()

    # 切换到frame中操作元素
    frame_test.switch_to_frame()
