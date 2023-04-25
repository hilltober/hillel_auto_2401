from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver: WebDriver, name: str):
        self.driver = driver
        self.locator = '//label[.="{}"]//ancestor::div[contains(@class, "radio")]'.format(name)
        self.input_ = '/input'
        self.label = '/label'

    def is_selected(self) -> bool:
        element = self.driver.find_element(By.XPATH, f'{self.locator}{self.input_}')
        return element.is_selected()

    def select(self) -> None:
        self.driver.find_element(By.XPATH, f'{self.locator}{self.label}').click()

    def enable(self) -> 'RadioButton':
        locator = (By.XPATH, f'{self.locator}{self.input_}')
        element = self.driver.find_element(*locator)
        if not element.is_enabled():
            self.driver.execute_script("arguments[0].disabled = false;", element)
        return self