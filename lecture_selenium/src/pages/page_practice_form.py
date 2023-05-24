from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PagePracticeForm:
    _instance = None
    URL = 'https://demoqa.com/automation-practice-form'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.__state_dropdown_loc = (By.ID, 'state')
        self.__state_input_loc = ''
        self.__city_dropdown_loc = ''
        self.__city_input_loc = ''

    def open(self) -> 'PagePracticeForm':
        self.driver.get(self.URL)
        return self

    def show_filtered_results_in_dropdown(self, keyword):
        element = self.driver.find_element(*self.__state_dropdown_loc)
        _ = element.location_once_scrolled_into_view
        element.click()
        state_input = element.find_element(By.XPATH, '//div[@id="state"]//input')
        state_input.send_keys(keyword)
        return state_input

    def get_results_from_dropdown(self):
        locator = (By.XPATH, '//div[contains(@class, "option")]')
        elements = self.driver.find_elements(*locator)
        return [element.text for element in elements]

    def set_state_via_input(self):
        state = 'Haryana'
        state_input = self.show_filtered_results_in_dropdown(state)
        state_input.send_keys(Keys.ENTER)

    def set_state_from_dropdown(self):
        state = 'Haryana'
        element = self.driver.find_element(*self.__state_dropdown_loc)
        _ = element.location_once_scrolled_into_view
        element.click()
        target_state = self.driver.find_element(
            By.XPATH, '//div[contains(@class, "-menu")]//div[contains(@id, "option")]'
                      f'[text()="{state}"]')
        target_state.click()
