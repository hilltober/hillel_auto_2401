from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lecture_selenium.src.helper.elements import get_appeared_element


class PageDynamicProperties:
    URL = 'https://demoqa.com/dynamic-properties'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.disabled_enabled_button_loc = (By.CSS_SELECTOR, 'button#enableAfter')
        self.invisible_visible_button_loc = (By.CSS_SELECTOR, 'button#visibleAfter')

    def open(self) -> 'PageDynamicProperties':
        self.driver.get(self.URL)
        return self

    def button_appeared(self) -> WebElement:
        button = get_appeared_element(self.driver, self.invisible_visible_button_loc, 5, poll=0.2)
        return button

    def button_disabled_enabled(self) -> WebElement:
        button = self.driver.find_element(*self.disabled_enabled_button_loc)
        return button

    def button_colored(self) -> WebElement:
        pass
