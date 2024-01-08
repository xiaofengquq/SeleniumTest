class TestData:
    def __init__(self, url=None, expect=None, status="run", parameters=None):
        self.url = url
        self.expect = expect
        self.status = status
        if parameters is None:
            parameters = {}
        self.parameters = parameters
        self.is_skip = False

    def get_parameters_value(self, value):
        return self.parameters[value]

    def to_string(self):
        # 使用f-string来格式化对象的状态
        return f"TestData(url='{self.url}', expect='{self.expect}', status='{self.status}', is_skip={self.is_skip}, parameters={self.parameters})"
