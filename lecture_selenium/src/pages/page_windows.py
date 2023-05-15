from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.widgets.button import Button


class WindowsPage(object):
    URL = 'https://demoqa.com/browser-windows'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> 'WindowsPage':
        self.driver.get(self.URL)
        return self

    def open_new_tab(self) -> None:
        button_open_tab = Button(self.driver, (By.ID, 'tabButton'))
        button_open_tab.click()

    def open_new_window(self) -> None:
        button_open_window = Button(self.driver, (By.ID, 'windowButton'))
        button_open_window.click()

    def open_window_message(self) -> None:
        button_window_message = Button(self.driver, (By.ID, 'messageWindowButton'))
        button_window_message.click()

