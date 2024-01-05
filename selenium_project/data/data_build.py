import os

import pandas as pd
from selenium import webdriver

from selenium_project.data.test_data import TestData
from selenium_project.util.util import Util

url = None
url_found = False
except_column = None
assert_column = None
status_column = None
test_data_list = []
parameters_column = {}
keys = []
mapping_tables = {
    "Util": Util
}


class DataBuild:
    @staticmethod
    def data_build(sheet_name: str, driver: webdriver) -> test_data_list:
        global url, url_found, except_column, assert_column, status_column, keys
        dir_path = os.path.dirname(os.path.abspath(__file__))
        xls_path = os.path.join(dir_path, 'selenium_test.xls')
        df = pd.read_excel(xls_path, header=None, sheet_name=sheet_name)
        # 遍历Excel
        for index, row in df.iterrows():

            # 创建一个空字典用于存储参数
            parameters = {}

            # 如果还没有找到URL，则进行URL解析
            if not url_found:
                if str(row[0]).lower() == 'url':
                    url = row[1]
                    url_found = True
                    continue
                else:
                    raise Exception('URL解析错误，请检查Excel')
            # 创建一个TestData实例
            test_data = TestData()

            # 如果当前行索引为1，即第二行，处理参数名
            if index == 1:
                keys = []
                count = -1
                for key in row:
                    count += 1
                    # 将键转换为字符串
                    key_string = str(key)
                    # 如果键以$开头，则添加到keys列表中，并创建列索引
                    if key_string.startswith('$'):

                        keys.append(key_string[1:])
                        parameters_column[key_string[1:]] = count
                    # 如果键不是以$开头，检查是否是expect、assert或status
                    else:
                        if key_string.lower() == 'expect':
                            except_column = count
                        elif key_string.lower() == 'assert':
                            assert_column = count
                        elif key_string.lower() == 'status':
                            status_column = count
                continue
            # 第三行开始为参数
            test_data.url = url
            test_data.id = pd.to_numeric(index) - 2

            for key in keys:
                # 从row字典的parameters_column键对应的列中读取值
                value = row[parameters_column[key]]
                # 如果读到的值是NaN，则转换为空字符串
                if pd.isna(value):
                    parameters[key] = ''
                    continue
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
                        # 调用方法，并将结果存储在parameters字典中
                        parameters[key] = function(*params)
                else:
                    # 如果值不以$开头或者不包含括号，则直接将值存储在parameters字典中
                    parameters[key] = value

            test_data.parameters = parameters
            test_data.expect = row[except_column]
            test_data.assert_ = row[assert_column]
            test_data.status = row[status_column]
            test_data_list.append(test_data)
        return test_data_list


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/user/register')
    test_data_list = DataBuild.data_build('register', driver)
    for test_data in test_data_list:
        print(test_data.to_string())
    # print(driver.find_element(By.CSS_SELECTOR, 'img').rect)
