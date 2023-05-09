from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.widgets.radio_button import RadioButton


class PageRadioButtonWithWidgets:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def select_radio_button(self, name):
        radio_button = RadioButton(self.driver, name)
        radio_button.select()

    def enable_element_if_disabled(self, name):
        button = RadioButton(self.driver, name)
        button.enable()







