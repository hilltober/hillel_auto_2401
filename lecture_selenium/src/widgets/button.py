from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.widgets.base_widget import Component


class Button(Component):

    def __init__(self, driver: WebDriver = None, locator: tuple = None):
        super().__init__(driver=driver, locator=locator)

    def hover(self):
        self._actions.move_to_element(self.element).perform()

    def click(self):
        self.element.click()

    def doubleclick(self):
        self._actions.double_click(self.element).perform()

    def get_attribute(self, attr):
        return self.element.get_attribute(attr)
