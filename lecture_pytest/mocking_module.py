class MyMock:
    mock_field = 'default'


class MockingClass(MyMock):

    def my_func(self):
        return self.mock_field
