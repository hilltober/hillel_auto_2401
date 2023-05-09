from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckbox:
    _instance = None
    URL = 'https://demoqa.com/checkbox'

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.folder_loc = '//label[contains(@for, "tree-node-{folder}")]'
        self.folder_expand_button_loc = f'{self.folder_loc}//ancestor::span/button'
        self.expand_status_loc = '//*[contains(@class, "expand-{}")]'
        self.folder_checkbox_input_loc = f'{self.folder_loc}/input'

    def open(self) -> 'PageCheckbox':
        self.driver.get(self.URL)
        return self


