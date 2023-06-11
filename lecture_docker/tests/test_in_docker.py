import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    yield driver
    driver.quit()


class TestDocker:

    def test_docker_selenium(self, chrome):
        chrome.get('https://google.com')
        assert chrome.find_element(By.XPATH, '//img[@alt="Google"]').is_displayed()

    def test_docker2(self):
        assert True

    def test_docker3(self):
        assert True
