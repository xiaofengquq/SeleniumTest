import os
import pandas as pd
from selenium_project.data.test_data import TestData


class DataBuild:
    @staticmethod
    def data_build():
        dir_path = os.path.dirname(os.path.abspath(__file__))
        xls_path = os.path.join(dir_path, 'selenium_test.xls')
        df = pd.read_excel(xls_path, header=None, sheet_name='register')

        test_cases = []  # 用于存储所有的TestData对象

        # 初始化一个字典，用于存储已经赋值的字段
        fields = {}

        for index, row in df.iterrows():
            # 创建一个新的TestData对象
            test_data = TestData()

            # 设置属性
            test_data.id = index

            # 处理URL
            if row[0] == 'URL':
                test_data.url = row[1]

            # 处理其他字段
            for col_num, value in enumerate(row[2:]):
                if '$' in str(value):
                    # 提取键和值
                    key, value = value.split('$')
                    fields[key] = value
                elif value == value and value is not None:  # 过滤掉NaN值和空字符串
                    # 如果该字段尚未赋值，则进行赋值
                    if col_num == 1 and row[col_num] == 'Expect':
                        test_data.expect = value
                    elif col_num == 2 and row[col_num] == 'Assert':
                        test_data.assert_ = value
                    elif col_num == 3 and row[col_num] == 'Setup':
                        test_data.setup = value
                    elif col_num == 4 and row[col_num] == 'Status':
                        test_data.status = value
                    elif col_num == 5 and row[col_num] == 'Description':
                        test_data.description = value
                    else:
                        # 如果这个字段不是期望、断言、设置、状态或描述，那么它就是一个参数
                        if col_num not in fields:
                            fields[col_num] = value
                        else:
                            # 如果该字段已经被赋值，那么更新它的值
                            fields[col_num] = value

            # 将参数字典的内容赋值到TestData的parameters属性中
            test_data.set_parameters(fields)

            # 添加到测试案例列表
            test_cases.append(test_data)

        # 打印所有测试案例的状态
        for test_data in test_cases:
            print(test_data.to_string())


if __name__ == '__main__':
    DataBuild.data_build()
