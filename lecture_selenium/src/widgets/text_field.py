from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lecture_selenium.src.widgets.base_widget import Component


class TextField(Component):

    def __init__(self, driver: WebDriver, locator: tuple):
        super().__init__(driver=driver, locator=locator)
        self.__actions = ActionChains(driver=driver)
        self.field: WebElement = self.driver.find_element(*self.locator)

    def clear(self) -> None:
        self.field.clear()

    def set_value(self, value: str) -> None:
        self.clear()
        self.field.send_keys(value)

    def send_keys(self, val: str) -> None:
        self.field.send_keys(val)

    def get_value(self) -> str:
        return self.field.get_attribute('value')

    def value_of_css_property(self, prop: str) -> str:
        return self.field.value_of_css_property(property_name=prop)
