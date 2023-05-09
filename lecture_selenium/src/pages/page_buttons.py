from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.widgets.button import Button


class PageButtons:
    _instance = None
    URL = 'https://demoqa.com/buttons'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.__button_doubleclick_loc = (By.ID, 'doubleClickBtn')
        self.__button_right_click_loc = (By.ID, 'rightClickBtn')
        self.__button_dynamic_id_loc = (By.XPATH, '//button[.="Click Me"]')
        self.__button_doubleclick_message_loc = (By.ID, 'doubleClickMessage')
        self.__button_right_click_message_loc = (By.ID, 'rightClickMessage')
        self.__button_dynamic_id_message_loc = (By.ID, 'dynamicClickMessage')

    def open(self) -> 'PageButtons':
        self.driver.get(self.URL)
        return self

    def button_doubleclick(self) -> Button:
        return Button(self.driver, self.__button_doubleclick_loc)

    def button_right_click(self) -> Button:
        return Button(self.driver, self.__button_right_click_loc)

    def button_dynamic_id(self) -> Button:
        return Button(self.driver, self.__button_dynamic_id_loc)

    def __get_element_text(self, locator: tuple) -> str | None:
        try:
            return self.driver.find_element(*locator).text
        except NoSuchElementException:
            return None

    def get_button_doubleclick_message(self):
        return self.__get_element_text(self.__button_doubleclick_message_loc)

    def get_button_right_click_message(self):
        return self.__get_element_text(self.__button_right_click_message_loc)

    def get_button_dynamic_id_message(self):
        return self.__get_element_text(self.__button_dynamic_id_message_loc)
