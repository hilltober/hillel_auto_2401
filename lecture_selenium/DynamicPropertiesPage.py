from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageDynamicProperties:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.disabled_enabled_button_loc = (By.CSS_SELECTOR, 'button#enableAfter')
        self.invisible_visible_button_loc = (By.CSS_SELECTOR, 'button#visibleAfter')

    def open(self):
        self.driver.get('https://demoqa.com/dynamic-properties')
        return self

    def button_invisible_visible(self) -> WebElement:
        button = self.driver.find_element(*self.invisible_visible_button_loc)
        return button

    def button_disabled_enabled(self) -> WebElement:
        button = self.driver.find_element(*self.disabled_enabled_button_loc)
        return button
