from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.widgets.base_widget import Component


class CheckBox(Component):
    def __init__(self, driver: WebDriver, locator: tuple, name: str = None):
        super().__init__(driver, locator)
        self.locator = locator
        by, loc = locator
        self.label = self.driver.find_element(by, loc)
        self.input_loc = '//input[@type="checkbox"]'
        self.input = self.label.find_element(By.XPATH, self.input_loc)
        self.named_label = '[contains(@for, "{}")]'
        self.named_input = '[contains(@id, "{}")]'
        if name:
            loc += self.named_label.format(name)
            self.label = self.driver.find_element(by, loc)
            self.input = self.label.find_element(By.XPATH, f'{self.input_loc}{self.named_input.format(name)}')
        # replace value in double-quotes with new value: re.sub(r'"[^"]+"', f'"new_val"', loc)

    def type_of(self) -> str:
        return self.__class__.__name__

    def __change_checkbox_selection_state(self, name: str) -> None:
        by, loc = self.locator
        if name:
            loc += self.named_label.format(name)
        label = self.driver.find_element(by, loc)
        label.click()

    def is_selected(self, name: str = None) -> bool:
        if name:
            input_loc = f'{self.input_loc}{self.named_input.format(name)}'
            input_ = self.label.find_element(By.XPATH, input_loc)
            return input_.is_selected()
        return self.input.is_selected()

    def select(self, name: str) -> None:
        if not self.is_selected(name):
            self.__change_checkbox_selection_state(name)

    def deselect(self, name: str) -> None:
        if self.is_selected(name):
            self.__change_checkbox_selection_state(name)
