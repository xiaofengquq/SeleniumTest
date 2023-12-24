class TestData:
    def __init__(self, id=None, url=None, expect=None, assert_=None, setup=None, status="run", description=None,
                 parameters=None):
        self.id = id
        self.url = url
        self.expect = expect
        self.assert_ = assert_
        self.setup = setup
        self.status = status
        self.description = description
        if parameters is None:
            parameters = {}
        self.parameters = parameters

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, parameters):
        self.parameters = parameters

    def to_string(self):
        # 使用f-string来格式化对象的状态
        return f"TestData(id={self.id}, url='{self.url}', expect='{self.expect}', assert_='{self.assert_}', setup='{self.setup}', status='{self.status}', description='{self.description}', parameters={self.parameters})"
