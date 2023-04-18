import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures('chrome')
class TestTextCheckbox:
    URL = 'https://demoqa.com/checkbox'

    def setup_method(self):
        self.driver: WebDriver = self.driver

    def open(self):
        self.driver.get(self.URL)

    def expand_folder(self, name):
        home = self.driver.find_element(By.XPATH, f'//label[contains(@for, "tree-node-{name}")]//ancestor::span/button')
        try:
            expand = home.find_element(By.XPATH, '//*[contains(@class, "expand-open")]')
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        home.click()

    def collapse_folder(self, name):
        home = self.driver.find_element(By.XPATH, f'//label[contains(@for, "tree-node-{name}")]//ancestor::span/button')
        try:
            collapse = home.find_element(By.XPATH, '//*[contains(@class, "expand-close")]')
            if collapse.is_displayed():
                collapse.click()
        except NoSuchElementException:
            pass
        home.click()

    def change_folder_selection_state(self, name, enabled=False):
        folder_loc = f'//label[contains(@for, "tree-node-{name}")]'
        input_loc = f'{folder_loc}/input'
        home = self.driver.find_element(By.XPATH, folder_loc)
        input_el = self.driver.find_element(By.XPATH, input_loc)
        if enabled:
            if not input_el.is_selected():
                home.click()
                return True
        else:
            if input_el.is_selected():
                home.click()
                return False

    def mark_folder(self, name):
        return self.change_folder_selection_state(name, enabled=True)

    def unmark_folder(self, name):
        return self.change_folder_selection_state(name, enabled=False)

    def test_checkbox_1(self):
        self.open()
        self.expand_folder('home')
        self.collapse_folder('home')
        assert self.mark_folder('home')
        assert not self.unmark_folder('home')
