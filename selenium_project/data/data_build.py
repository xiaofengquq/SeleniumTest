import os
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

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
        for index, row in df.iterrows():
            parameters = {}
            if not url_found:
                if str(row[0]).lower() == 'url':
                    url = row[1]
                    url_found = True
                    continue
                else:
                    raise Exception('URL解析错误，请检查Excel')
            test_data = TestData()
            if index == 1:
                keys = []
                count = -1
                for key in row:
                    count += 1
                    key_string = str(key)
                    if str.startswith(key_string, '$'):
                        keys.append(key_string[1:])
                        parameters_column[key_string[1:]] = count
                    else:
                        if key_string.lower() == 'expect':
                            except_column = count
                        elif key_string.lower() == 'assert':
                            assert_column = count
                        elif key_string.lower() == 'status':
                            status_column = count
                continue

            test_data.url = url
            test_data.id = pd.to_numeric(index) - 2

            for key in keys:
                value = row[parameters_column[key]]
                if pd.isna(value):
                    parameters[key] = ''
                    continue
                if str(value).startswith('$'):
                    if '(' in str(value):
                        # 假设我们有以下字符串，其中包含方法名和参数
                        method_call_str = value[1:]
                        # 分割字符串以获取方法名和参数列表
                        parts = method_call_str.split('(')
                        class_name = parts[0].split('.')[0].strip()
                        method_name = parts[0].split('.')[1].strip()
                        params = parts[1].split(',')
                        params = [param.strip() for param in params]  # 去除每个参数两端的空白字符.
                        if params[-1].endswith(')'):
                            params[-1] = params[-1][:-1]
                        function = getattr(mapping_tables[class_name], method_name)
                        for i, param in enumerate(params):
                            if param == '$driver':
                                params[i] = driver
                            elif param == '$None':
                                params[i] = None
                        # print(f'params: {params}')
                        parameters[key] = function(*params)
                else:
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
