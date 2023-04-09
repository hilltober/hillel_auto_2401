import pytest


@pytest.fixture(scope='function', autouse=True)
def package_fixture1():
    yield


@pytest.fixture(scope='class', autouse=True)
def package_fixture2():
    yield


@pytest.fixture(scope='package', autouse=True)
def package_fixture3():
    yield


@pytest.fixture(scope='session', autouse=True)
def package_fixture4():
    yield
