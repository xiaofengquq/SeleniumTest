import os.path
import unittest


class TestCase01(unittest.TestCase):

    # 类方法，在运行任何测试之前被调用一次，用于初始化测试环境
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass start')

    # 类方法，在所有测试运行完成后被调用一次，用于清理测试环境
    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass start')

    def test01(self):
        print('test01 starts')
        self.assertTrue(True)

    def test02(self):
        print('test02 starts')
        self.assertTrue(False)


class TestCase02(unittest.TestCase):
    def test03(self):
        print('test03 starts')
        self.assertTrue(False)

    def test04(self):
        print('test04 starts')
        self.assertTrue(True)

# # 当这个模块作为主程序运行时，以下代码块将被执行
# if __name__ == '__main__':
#     # 创建一个测试加载器，用于加载测试用例
#     loader = unittest.TestLoader()
#     # 创建一个测试套件，用于存放加载的测试用例
#     suite = unittest.TestSuite()
#     # # 将TestCase01中的测试用例添加到测试套件中
#     # suite.addTest(loader.loadTestsFromTestCase(TestCase01))
#     # # 将TestCase02中的测试用例添加到测试套件中
#     # suite.addTest(loader.loadTestsFromTestCase(TestCase02))
#
#     #   用更简便的方式添加测试用例
#     #   通过当前文件的父目录来加载
#     dirpath = os.path.dirname(os.path.abspath(__file__))
#     suite.addTest(loader.discover(dirpath))
#
#     # 创建一个文本测试运行器，用于运行测试套件中的测试用例
#     runner = unittest.TextTestRunner()
#     # 运行测试套件中的所有测试用例
#     runner.run(suite)
