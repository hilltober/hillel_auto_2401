import pytest

from lecture_selenium.src.widgets.radio_button import RadioButton


@pytest.mark.usefixtures('chrome')
class TestRadioButton:
    def test_widget(self):
        self.driver.get('https://demoqa.com/radio-button')

        radio_button_yes = RadioButton(driver=self.driver, name='Yes')
        radio_button_yes.select()
        a = radio_button_yes.is_selected()
        radio_button_no = RadioButton(self.driver, name='No')
        radio_button_no.enable().select()
        b = radio_button_no.is_selected()
        assert a and b
