from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageAlerts:
    _instance = None
    URL = 'https://demoqa.com/alerts'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.__base_alert_loc = (By.ID, 'alertButton')
        self.__timer_alert_loc = (By.ID, 'timerAlertButton')
        self.__confirm_alert_loc = (By.ID, 'confirmButton')
        self.__prompt_alert_loc = (By.ID, 'promtButton')
        self.__alert_confirm_result_loc = (By.ID, 'confirmResult')
        self.__alert_prompt_result_loc = (By.ID, 'promptResult')

    def open(self) -> 'PageAlerts':
        self.driver.get(self.URL)
        return self

    def open_base_alert(self) -> None:
        alert_button = self.driver.find_element(*self.__base_alert_loc)
        alert_button.click()

    def open_timer_alert(self) -> None:
        alert_button = self.driver.find_element(*self.__timer_alert_loc)
        alert_button.click()

    def open_confirm_alert(self) -> None:
        alert_button = self.driver.find_element(*self.__confirm_alert_loc)
        alert_button.click()

    def open_prompt_alert(self) -> None:
        alert_button = self.driver.find_element(*self.__prompt_alert_loc)
        alert_button.click()

    def get_confirm_result(self) -> str:
        result = self.driver.find_element(*self.__alert_confirm_result_loc).text
        return result

    def get_prompt_result(self) -> str:
        result = self.driver.find_element(*self.__alert_prompt_result_loc).text
        return result
