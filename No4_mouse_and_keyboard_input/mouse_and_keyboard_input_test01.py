import traceback
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.by import By


# 模拟鼠标

class FormTest07:
    def __init__(self):
        # 初始化 WebDriver、ActionChains 和 WebDriverWait
        self.driver = webdriver.Chrome()
        # 打开单击测试页面
        self.driver.get('https://sahitest.com/demo/clicks.htm')
        self.ac = AC(self.driver)

    def perform_action_and_check_text(self, action: str, ac: AC, expected_text: str):
        try:
            # 执行操作前先找到清空按钮
            clear = self.driver.find_element(By.NAME, 't1')
            ac.perform()
            # 执行操作后再找到文本框
            textBox = self.driver.find_element(By.NAME, 't2')
            actual_text = textBox.get_attribute('value')
            # 检查文本是否符合预期
            if expected_text in actual_text:
                print(f'成功 {action} 并获取文本框文本为 [{expected_text}]')
            else:
                raise Exception(f'执行 {action} 后未找到预期文本 {expected_text}, 当前文本为 {actual_text}')
            sleep(2)
            # 执行清空操作，保证每次找到的文本都是最新触发的
            ac.click(clear).perform()

        except:
            traceback.print_exc()

    def test_mouse_input(self):
        # 找到需要进行点击、双击、右键单击的元素
        clear = self.driver.find_element(By.NAME, 't1')
        click = self.driver.find_element(By.XPATH, '/html/body/No2_form/input[3]')
        double_click = self.driver.find_element(By.XPATH, '/html/body/No2_form/input[2]')
        right_click = self.driver.find_element(By.XPATH, '/html/body/No2_form/input[4]')

        # 分别执行点击、清空文本框、双击、右键单击操作
        self.perform_action_and_check_text('清空文本框', self.ac.click(clear), '')
        self.perform_action_and_check_text('单击', self.ac.click(click), '[CLICK]')
        self.perform_action_and_check_text('双击', self.ac.double_click(double_click), '[DOUBLE_CLICK]')
        self.perform_action_and_check_text('右键单击', self.ac.context_click(right_click), '[RIGHT_CLICK]')


if __name__ == '__main__':
    # 实例化 FormTest07 类并执行测试
    form_test = FormTest07()
    sleep(1)
    # 移动到多选第二个选项并点击
    element = form_test.driver.find_element(By.XPATH, '/html/body/No2_form/input[8]')
    form_test.ac.move_to_element(element).click().perform()
    sleep(2)
    form_test.test_mouse_input()
