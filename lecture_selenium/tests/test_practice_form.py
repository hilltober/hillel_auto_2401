import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lecture_selenium.src.pages.page_practice_form import PagePracticeForm


@pytest.mark.usefixtures('chrome')
class TestPracticeForm:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PagePracticeForm(self.driver)

    def test_(self):
        self.page.open()
        # self.page.set_state_via_input()
        self.page.set_state_from_dropdown()
        self.page.show_filtered_results_in_dropdown('Har')
        results = self.page.get_results_from_dropdown()
        is_ok = all(['Har' in result for result in results])
        assert is_ok

    def test_upload_file_v1(self):
        self.page.open()
        upload_button_input = self.driver.find_element(By.CSS_SELECTOR, 'input#uploadPicture')
        upload_button_input.send_keys('C:\\Users\\tober\\Pictures\\selenium_python.png')
        txt = upload_button_input.get_attribute('value')
        assert 'selenium_python.png' in txt
