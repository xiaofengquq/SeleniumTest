import pytest


class TestCase02(object):
    def test01(self):
        print('test01')
        assert True

    def test02(self):
        print('test02')
        assert False

    def test03(self):
        print('test03')
        assert False


#
if __name__ == '__main__':
    pytest.main(['-vsx', 'pytest_test.py'])
