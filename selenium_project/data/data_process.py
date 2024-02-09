import os

from selenium import webdriver

from selenium_project.data.data_read import DataRead
from selenium_project.util.util import Util

mapping_tables = {
    "Util": Util
}
keys = []
parameters_column = {}


class DataProcess:
    @staticmethod
    def data_process(test_data, driver: webdriver):
        for key, value in test_data.parameters.items():
            # 如果值以$开头并且包含括号，则认定为需要调用方法
            if str(value).startswith('$'):
                if '(' in str(value):
                    # 获取方法调用字符串，去掉开头的$
                    method_call_str = value[1:]
                    # 将方法调用字符串按照左括号分割为两部分
                    parts = method_call_str.split('(')
                    # 获取类名
                    class_name = parts[0].split('.')[0].strip()
                    # 获取方法名
                    method_name = parts[0].split('.')[1].strip()
                    # 将参数部分按照逗号分割为参数列表
                    params = parts[1].split(',')
                    params = [param.strip() for param in params]
                    if params[-1].endswith(')'):
                        # 如果参数列表的最后一个元素以右括号结尾，则移除右括号
                        params[-1] = params[-1][:-1]
                    try:
                        # 尝试从mapping_tables字典中获取类名对应的方法
                        function = getattr(mapping_tables[class_name], method_name)
                    except:
                        # 如果方法不存在，抛出异常
                        raise Exception('未在指定模块中找到指定方法，请检查Excel')
                    for i, param in enumerate(params):
                        # 如果参数是$driver，则替换为实际的driver变量
                        if param == '$driver':
                            params[i] = driver
                        # 如果参数是$None，则替换为None
                        elif param == '$None':
                            params[i] = None
                        # 如果参数是$True，或者$False，则替换为True或False
                        elif param == '$True':
                            params[i] = True
                        elif param == '$False':
                            params[i] = False
                    # 调用方法，并将结果赋值回parameters字典中
                    test_data.parameters[key] = function(*params)
        # 返回处理完毕的 test_data
        return test_data


if __name__ == '__main__':
    driver = webdriver.Chrome()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    xls_path = os.path.join(dir_path, 'selenium_test.xls')
    test_data_list = DataRead.data_read(xls_path, 'register')
    for data in test_data_list:
        driver.get(data.url)
        data = DataProcess.data_process(data, driver)
        print(data.to_string())
