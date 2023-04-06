from unittest.mock import patch, MagicMock

from pytest_mock import MockerFixture


def ignored_func() -> str:
    return 'some_ignored_string'


def test_can_mock_ignored_func_with_default_mock():
    with patch(target='lecture_pytest.tests.test_mocks.ignored_func',
               return_value='some_mocked_str'):
        assert ignored_func() == 'some_mocked_str'
    assert ignored_func() == 'some_ignored_string'


def test_can_mock_ignored_func_with_pytest_mock(mocker: MockerFixture):
    mocker.patch(target='lecture_pytest.tests.test_mocks.ignored_func',
                 return_value='another_mocked_str')
    assert ignored_func() == 'another_mocked_str'


class Config:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint


class MyClass:
    def __init__(self, config):
        self.config = config

    def get_url(self, path):
        return f"{self.config.endpoint}/{path}?api_key={self.config.api_key}"


def test_get_url():
    config_mock = MagicMock(spec=Config)
    config_mock.api_key = 'test_key'
    config_mock.endpoint = 'https://api.example.com'
    my_class = MyClass(config_mock)

    url = my_class.get_url('path')
    assert url == 'https://api.example.com/path?api_key=test_key'
    assert config_mock.api_key == 'test_key'
    assert config_mock.endpoint == 'https://api.example.com'
