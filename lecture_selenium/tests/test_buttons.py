import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.pages.page_buttons import PageButtons


@pytest.mark.usefixtures('chrome')
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButtons(driver=self.driver)
        self.page.open()

    def test_doubleclick_button(self):
        self.page.button_doubleclick().doubleclick()
        assert 'double click' in self.page.get_button_doubleclick_message()

    def test_right_click_button(self):
        self.page.button_right_click().right_click()
        assert 'right click' in self.page.get_button_right_click_message()

    def test_dynamic_id_button(self):
        self.page.button_dynamic_id().click()
        assert 'dynamic click' in self.page.get_button_dynamic_id_message()
