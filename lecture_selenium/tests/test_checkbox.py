import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.pages.page_checkbox import PageCheckbox


@pytest.mark.usefixtures('chrome')
class TestCheckbox:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageCheckbox(self.driver).open()

    def test_checkbox_1(self):
        self.page.expand_folder('home')
        self.page.collapse_folder('home')
        assert self.page.mark_folder('home')
        assert self.page.unmark_folder('home')
