import os.path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# 测试 表单复选，单选

class FormTest03(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        dir_path = os.path.dirname(os.path.abspath(__file__))
        self.path = 'file:///' + os.path.join(dir_path, 'forms_test.html')
        self.driver.get(self.path)

    def test_select(self):
        sleep(1)
        se = self.driver.find_element(value='province')
        select = Select(se)
        # 通过下标选择第三个option元素
        select.select_by_index(2)
        sleep(1)
        # 通过值选择value为tj的元素
        select.select_by_value('tj')
        sleep(1)
        # 通过可见文本选择 北京
        select.select_by_visible_text('北京')
        sleep(1)

        se1 = self.driver.find_element(value='cars')
        select1 = Select(se1)
        options = select1.options
        selected_options = []
        # 遍历options全选下拉框
        for option in options:
            option.click()
            selected_options.append(option.text)
        sleep(2)
        print(f'所有选中选项: {selected_options}')
        # 使用index反选
        for i in range(3, 0, -1):
            option = select1.options[0]
            select1.deselect_by_index(i)
            if option.is_selected():
                print(f'第一个选择选项：{select1.first_selected_option.text}')
            sleep(1)


if __name__ == '__main__':
    form_test = FormTest03()
    form_test.test_select()
