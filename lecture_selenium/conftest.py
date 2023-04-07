import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.close()
