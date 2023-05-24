import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lecture_selenium.src.pages.page_alerts import PageAlerts


@pytest.mark.usefixtures('chrome')
@pytest.mark.alerts
class TestAlerts:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageAlerts(driver=self.driver)
        self.page.open()

    def test_base_alert(self):
        self.page.open_base_alert()
        alert = self.driver.switch_to.alert
        txt = alert.text
        alert.accept()
        assert 'clicked' in txt

    def test_timer_alert(self):
        self.page.open_timer_alert()
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        txt = alert.text
        alert.accept()
        assert 'appeared' in txt

    def test_accept_confirm_alert(self):
        self.page.open_confirm_alert()
        alert = self.driver.switch_to.alert
        txt = alert.text
        alert.accept()
        assert 'confirm' in txt
        assert 'Ok' in self.page.get_confirm_result()

    def test_decline_confirm_alert(self):
        self.page.open_confirm_alert()
        alert = self.driver.switch_to.alert
        txt = alert.text
        alert.dismiss()
        assert 'confirm' in txt
        assert 'Cancel' in self.page.get_confirm_result()
