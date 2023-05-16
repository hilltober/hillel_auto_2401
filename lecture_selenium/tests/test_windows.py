import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.pages.page_windows import WindowsPage


@pytest.mark.usefixtures('firefox')
class TestWindows:

    @pytest.fixture(scope='function')
    def windows_fixture(self):
        default_page = self.driver.current_window_handle
        yield default_page
        self.driver.close()
        self.driver.switch_to.window(default_page)

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = WindowsPage(driver=self.driver)
        self.page.open()

    def test_tab(self, windows_fixture):
        self.page.open_new_tab()
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        text = self.driver.find_element(By.ID, 'sampleHeading').text
        assert 'sample' in text

    def test_window(self, windows_fixture):
        self.page.open_new_window()
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        text = self.driver.find_element(By.ID, 'sampleHeading').text
        assert 'page' in text
