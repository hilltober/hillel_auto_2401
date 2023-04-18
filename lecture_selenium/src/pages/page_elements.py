from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ElementsPage(object):
    URL = 'https://demoqa.com/elements'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super.__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.element_categories = By.XPATH, '//div[contains(@class, "show")]//li'

    def open(self) -> 'ElementsPage':
        self.driver.get(self.URL)
        return self

    def get_elements_page_categories(self) -> list:
        categories = [cat.text for cat in self.driver.find_elements(*self.element_categories)]
        return categories
