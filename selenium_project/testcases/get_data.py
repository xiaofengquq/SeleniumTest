import os.path

import pandas as pd
from selenium import webdriver


class GetData:
    @staticmethod
    def get_data():
        df = None
        try:
            df = pd.read_excel("D:\PycharmProjects\SeleniumTest\selenium_project\data\selenium_test.xls", header=None)
        except Exception as e:
            print(e)
        for index, row in df.iterrows():
            print(row[1])


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    xls_path = os.path.join(dir_path, 'data1', 'selenium_test.xls')
    print(xls_path)
    GetData.get_data()
