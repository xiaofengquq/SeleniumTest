class TestData:
    def __init__(self, id=None, url=None, expect=None, assert_=None, status="run", parameters=None):
        self.id = id
        self.url = url
        self.expect = expect
        self.assert_ = assert_
        self.status = status
        if parameters is None:
            parameters = {}
        self.parameters = parameters
        self.is_skip = False

    def get_parameters_value(self, value):
        return self.parameters[value]

    def to_string(self):
        # 使用f-string来格式化对象的状态
        return f"TestData(id={self.id}, url='{self.url}', expect='{self.expect}', assert_='{self.assert_}', status='{self.status}', is_skip={self.is_skip}, parameters={self.parameters})"
