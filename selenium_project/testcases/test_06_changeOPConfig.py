from time import sleep
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 导入自定义的数据处理和数据读取模块
from selenium_project.data.data_process import DataProcess
from selenium_project.data.data_read import DataRead

# TestCase类用于封装测试用例
class TestCase:
    __driver = None  # 类变量，用于存储webdriver实例

    def setup_class(self):
        # 每次执行测试前初始化webdriver，并最大化窗口
        self.__driver = webdriver.Chrome()
        self.__driver.maximize_window()

    def teardown_class(self):
        # 每次执行测试后关闭webdriver
        self.__driver.quit()

    # 使用pytest.mark.parametrize装饰器，参数化测试数据
    @allure.story('修改后台配置')
    @pytest.mark.parametrize('data', DataRead.data_read('change_op_config'))
    def test_change_op_config(self, data):
        # 如果数据标记为跳过，则使用pytest.skip跳过测试
        if data.is_skip:
            pytest.skip("Data is marked to be skipped")

        # 打开注册页面
        self.__driver.get(data.url)

        # 对数据进行处理
        data = DataProcess.data_process(data, self.__driver)
        # 定位用户名输入框并输入用户名
        username = self.__driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        username.send_keys(data.get_parameters_value('username'))
        # 定位密码输入框并输入密码
        password = self.__driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password.send_keys(data.get_parameters_value('password'))
        # 定位登录按钮并点击
        self.__driver.find_element(By.CSS_SELECTOR, 'button[id="loginBtn"').click()
        # 定位并点击操作配置菜单
        self.__driver.find_element(By.CSS_SELECTOR, 'a[data-key="19"]').click()
        # 定位并点击礼品兑换规则页面链接
        self.__driver.find_element(By.CSS_SELECTOR, 'a[href="/gift_redeem/rule/page"]').click()
        # 定位iframe并切换到该iframe
        iframe = self.__driver.find_element(By.CSS_SELECTOR, 'iframe[src="/gift_redeem/rule/page"]')
        self.__driver.switch_to.frame(iframe)
        # 定位规则ID输入框并输入规则ID
        rule_id = self.__driver.find_element(By.ID, 'id')
        rule_id.send_keys(data.get_parameters_value('rule_id'))
        # WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.ID, 'searchBtn')))
        self.__driver.find_element(By.ID, 'searchBtn').click()
        # sleep(1)
        # edit = self.__driver.find_element(By.CSS_SELECTOR, 'button[onclick="editRowBefore(422)"]')
        # 使用显式等待来等待搜索按钮出现（使用 隐式等待 会导致页面所有元素都需要等待固定时间加载，会大大增加页面加载时间）
        edit = WebDriverWait(self.__driver, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[onclick="editRowBefore(422)"]')))
        # 定位并点击编辑按钮
        edit.click()

        # 线程休眠2秒，等待页面响应
        sleep(2)
        # # 断言弹窗文本与预期结果一致
        # assert alert_text == expect

# 注意事项：
# 1. 使用sleep可能会导致测试的不稳定，建议尽量使用显式等待。
# 2. 在查找元素之前，请确保元素所在的页面或框架已经被加载。
# 3. 如果遇到元素未找到的错误，请检查CSS选择器是否正确或元素是否存在于DOM中。
# 4. 在使用参数化测试时，请确保数据文件的格式正确，并且每个参数都有对应的测试数据。
