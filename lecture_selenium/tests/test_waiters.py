import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('firefox_fixture')
class TestWaiters:

    def setup_function(self):
        self.driver: WebDriver = self.driver

    def test_buttons(self):
        self.driver.get('https://demoqa.com/dynamic-properties')
        visible_invisible_button_loc = (By.CSS_SELECTOR, '#visibleAfter')
        WebDriverWait(self.driver, timeout=5).until(ec.visibility_of_element_located(visible_invisible_button_loc))
        visible_invisible_button = self.driver.find_element(*visible_invisible_button_loc)
        visible_invisible_button.click()
        enabled_disabled_button_loc = (By.CSS_SELECTOR, '#enableAfter')
        enabled_disabled_button = self.driver.find_element(*enabled_disabled_button_loc)
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(enabled_disabled_button))
        enabled_disabled_button.click()
        colored_button_loc = (By.ID, 'colorChange')
        WebDriverWait(self.driver, 5).until(
            ec.text_to_be_present_in_element_attribute(colored_button_loc, 'class', 'text-danger'))
        colored_button = self.driver.find_element(colored_button_loc)
        colored_button.click()
        pass
