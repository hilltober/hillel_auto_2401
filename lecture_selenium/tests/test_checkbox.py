import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.pages.page_checkbox import PageCheckbox
from lecture_selenium.src.pages.page_text_box_with_widgets import PageRadioButtonWithWidgets


@pytest.mark.usefixtures('chrome')
class TestCheckbox:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        # self.page = PageCheckbox(self.driver).open()

    def test_checkbox_1(self):
        self.page.expand_folder('home')
        self.page.collapse_folder('home')
        assert self.page.mark_folder('home')
        assert self.page.unmark_folder('home')

    def test_checkbox_2(self):
        self.driver.get('https://demoqa.com/radio-button')
        page = PageRadioButtonWithWidgets(self.driver)
        page.select_radio_button('Yes')
        page.select_radio_button('Impressive')
        page.enable_element_if_disabled('No')
        page.select_radio_button('No')
        pass

