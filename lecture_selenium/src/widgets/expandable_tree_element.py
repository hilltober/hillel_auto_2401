import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.widgets.base_widget import Component


class ExpandableTreeElement(Component):

    def __init__(self, driver: WebDriver = None, locator: tuple = None, name: str = None):
        super().__init__(driver, locator)
        self.folder_loc = '//label[contains(@for, "tree-node-{folder}")]'
        if name:
            self.folder_loc = f'//label[contains(@for, "tree-node-{name}")]'
        self.folder_expand_button_loc = f'{self.folder_loc}//ancestor::span/button'
        self.expand_status_loc = '//*[contains(@class, "expand-{}")]'

    def __change_folder_expand_state(self, name: str = None, open_: bool = True) -> None:
        if name:
            folder = self.driver.find_element(By.XPATH, self.folder_expand_button_loc.format(folder=name))
        else:
            folder = self.driver.find_element(By.XPATH, self.folder_expand_button_loc)
        try:
            if open_:
                folder.find_element(By.XPATH, self.expand_status_loc.format('close')).click()
            else:
                folder.find_element(By.XPATH, self.expand_status_loc.format('open')).click()
        except NoSuchElementException:
            pass

    def expand_folder(self, name) -> None:
        self.__change_folder_expand_state(name=name, open_=True)

    def collapse_folder(self, name) -> None:
        self.__change_folder_expand_state(name=name, open_=False)

    def __change_folder_selection_state(self, name, enabled=False) -> bool:
        folder = self.driver.find_element(By.XPATH, self.folder_loc.format(folder=name))
        input_el = folder.find_element(By.XPATH, '//input')
        if enabled:
            if not input_el.is_selected():
                folder.click()
                return input_el.is_selected()
        else:
            if input_el.is_selected():
                folder.click()
                return not input_el.is_selected()

    def mark_folder(self, name) -> bool:
        state = self.__change_folder_selection_state(name, enabled=True)
        return state

    def unmark_folder(self, name) -> bool:
        state = self.__change_folder_selection_state(name, enabled=False)
        return state


@pytest.mark.usefixtures('chrome')
class TestWidgets:
    URL = 'https://demoqa.com/buttons'

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.driver.get(self.URL)
        pass
