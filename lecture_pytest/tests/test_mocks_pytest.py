from pytest_mock import MockerFixture

from lecture_pytest.mocking_module import MockingClass


def test_mock_func(mocker: MockerFixture):
    mocker.patch('lecture_pytest.mocking_module.MockingClass.my_func', return_value='redefined func text')
    print(MockingClass().my_func())


def test_mock_field(mocker: MockerFixture):
    mocker.patch.object(MockingClass, 'mock_field', 'mocked_value')
    print(MockingClass.mock_field)

