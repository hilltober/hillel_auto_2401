import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from lecture_selenium.DynamicPropertiesPage import PageDynamicProperties
from lecture_selenium.TextBoxPage import TextBoxPage


@pytest.mark.usefixtures('chrome')
class TestTextBoxPage:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = TextBoxPage(self.driver).open()

    def test_fullname(self):
        name = 'Vasya Pupkin'
        self.page.fill_full_name_field(name)
        self.page.click_submit()
        assert name in self.page.get_result_fullname()

    def test_email_positive(self):
        email = 'pupkin@gmail.com'
        self.page.fill_email_field(email)
        self.page.click_submit()
        assert email in self.page.get_result_email()

    def test_email_negative(self):
        email = 'pupkingmail.com'
        self.page.fill_email_field(email)
        self.page.click_submit()
        assert 'error' in self.page.get_email_field_element().get_attribute('class')

    def test_curr_address(self):
        address = 'Pupkin`s current addr'
        self.page.fill_current_address_field(address)
        self.page.click_submit()
        assert address in self.page.get_result_curr_addr()

    def test_perm_address(self):
        address = 'Pupkin`s perm addr'
        self.page.fill_permanent_address_field(address)
        self.page.click_submit()
        assert address == self.page.get_result_perm_addr()


@pytest.mark.usefixtures('chrome')
class TestDynamicElements:

    def setup_method(self) -> None:
        self.driver: WebDriver = self.driver
        self.page = PageDynamicProperties(self.driver).open()

    def test_is_button_enables_webdriver_wait(self):
        locator = self.page.disabled_enabled_button_loc
        button: WebElement = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(button))
        assert button.is_enabled()
        button.click()

    def test_is_button_enables_custom_wait(self):
        locator = self.page.disabled_enabled_button_loc
        button: WebElement = self.driver.find_element(*locator)
        assert self.is_element_enabled(button, timeout=5)

    @staticmethod
    def is_element_enabled(element: WebElement, timeout: int) -> bool:
        end_time = time.monotonic() + timeout
        while time.monotonic() <= end_time:
            if element.is_enabled():
                return True
            else:
                time.sleep(0.1)
        raise TimeoutError(f'Element is not enabled after {timeout} seconds')


@pytest.mark.parametrize('key,value',
                         [[1, int], [2.1, float], [True, bool]],
                         ids=['INTEGER', 'FLOAT', 'BOOLEAN'])
def test_types(key, value):
    assert type(key) is value
