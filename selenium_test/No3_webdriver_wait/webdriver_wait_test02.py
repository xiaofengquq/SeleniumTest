import os.path
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FormTest06(object):
    def __init__(self):
        # 初始化webdriver，加载本地HTML文件
        self.driver = webdriver.Chrome()
        dir_path = os.path.dirname(os.path.abspath(__file__))
        html_path = 'file:///' + os.path.join(dir_path, 'test_wait.html')
        self.driver.get(html_path)

    def test_wait(self):
        # 点击页面上的按钮
        self.driver.find_element(By.XPATH, '/html/body/No2_form/input[2]').click()

        # 使用WebDriverWait等待特定条件出现
        wait = WebDriverWait(self.driver, 3)
        try:
            # 等待id为'id2'的元素中的文本出现为'id 2'
            wait.until(EC.text_to_be_present_in_element((By.ID, 'id2'), 'id 2'), 'Element not found')
            print('ok')
        except:
            # 捕获异常并打印堆栈信息
            traceback.print_exc()


if __name__ == '__main__':
    # 创建FormTest06实例并调用test_wait方法
    form_test = FormTest06()
    form_test.test_wait()
