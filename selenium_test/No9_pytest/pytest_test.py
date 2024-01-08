import time

import pytest


class TestCase02:  # 定义一个名为TestCase02的类，用于组织测试用例
    @staticmethod
    def setup_class():  # 定义一个静态方法setup_class，该方法在类中的所有测试方法执行前运行一次
        print('setup_class run')  # 打印“setup_class run”，表示setup_class方法已经运行

    @staticmethod
    def teardown_class():  # 定义一个静态方法teardown_class，该方法在类中的所有测试方法执行后运行一次
        print('teardown_class run')  # 打印“teardown_class run”，表示teardown_class方法已经运行

    @pytest.fixture()  # 使用pytest.fixture装饰器定义一个fixture，名为init
    def init(self):  # 定义一个方法init，该方法在每次测试前运行
        print(time.strftime('%Y年%m月%d日 %H-%M-%S'))  # 打印当前时间，格式为“年月日 时分秒”

    @staticmethod
    def subtraction(x):  # 定义一个静态方法subtraction，用于执行减法操作
        return x - 1  # 返回x减1的结果

    # 参数化测试
    @pytest.mark.parametrize('data', [5, 6, 7])  # 使用pytest.mark.parametrize装饰器，为测试方法提供参数化数据
    def test01(self, data, init):  # 定义一个测试方法test01，该方法接受两个参数：data和init
        assert TestCase02.subtraction(data) == 5  # 断言subtraction方法返回的结果等于5
