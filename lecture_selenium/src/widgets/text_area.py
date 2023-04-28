from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.widgets.text_field import TextField


class TextArea(TextField):
    def __init__(self, driver: WebDriver, locator: tuple):
        super().__init__(driver, locator)
