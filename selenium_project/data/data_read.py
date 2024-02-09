import os

import pandas as pd

from selenium_project.data.test_data import TestData

url = None
url_found = False
except_column = None
status_column = None
test_data_list = []
parameters_column = {}
keys = []


class DataRead:
    @staticmethod
    def data_read(xls_path: str, sheet_name: str) -> test_data_list:
        global url, url_found, except_column, status_column, keys
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
            data = TestData()
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
                    # 如果键不是以$开头，检查是否是expect或者status
                    else:
                        if key_string.lower() == 'expect':
                            except_column = count
                        elif key_string.lower() == 'status':
                            status_column = count
                continue
            # 第三行开始为参数
            data.url = url
            for key in keys:
                # 从row字典的parameters_column键对应的列中读取值
                value = row[parameters_column[key]]
                # 如果读到的值是NaN，则转换为空字符串
                if pd.isna(value):
                    parameters[key] = ''
                else:
                    # 如果值不以$开头或者不包含括号，则直接将值存储在parameters字典中
                    parameters[key] = value
            data.parameters = parameters
            data.expect = row[except_column]
            data.status = row[status_column]
            if data.status == 'skip':
                data.is_skip = True
            test_data_list.append(data)
        return test_data_list


if __name__ == '__main__':
    test_data_list = DataRead.data_read('register')
    for data in test_data_list:
        print(data.to_string())
    # print(driver.find_element(By.CSS_SELECTOR, 'img').rect)
