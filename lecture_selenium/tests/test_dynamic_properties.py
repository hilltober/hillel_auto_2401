import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from lecture_selenium.src.pages.page_dynamic_properties import PageDynamicProperties


@pytest.mark.usefixtures('chrome')
class TestDynamicProperties:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageDynamicProperties(self.driver)
        self.page.open()

    def test_appeared_button(self):
        button = self.page.button_appeared()
        assert button.is_displayed()

    def test_enabled_disabled_button(self):
        button = self.page.button_disabled_enabled()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(button))
        assert button.is_enabled()
