import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture()
def firefox_fixture(request):
    driver: WebDriver = request.getfixturevalue('firefox')
    yield driver
    driver.quit()


@pytest.fixture()
def package_text_fixture(request):
    text = request.getfixturevalue('example_project_fixture')
    text += '6'
    yield text
