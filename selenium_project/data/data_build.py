import os
import pandas

from selenium_project.data.test_data import TestData


class DataBuild:
    @staticmethod
    def data_build():
        dir_path = os.path.dirname(os.path.abspath(__file__))
        xls_path = os.path.join(dir_path, 'selenium_test.xls')
        df = pandas.read_excel(xls_path, header=None, sheet_name='register')
        test_cases = []  # 用于存储所有的TestData对象
        for index, row in df.iterrows():
            # 创建一个新的TestData对象
            test_case = TestData()
            # 设置属性
            test_case.url = row[1] if row[0] == 'URL' else None
            test_case.id = index
            # 添加到测试案例列表
            test_cases.append(test_case)
        # 打印所有测试案例的状态
        for test_case in test_cases:
            print(test_case.to_string())


if __name__ == '__main__':
    DataBuild.data_build()
