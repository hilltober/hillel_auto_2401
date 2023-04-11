import pytest

from lecture_selenium.ElementsPage import ElementsPage
from lecture_selenium.TextBoxPage import TextBoxPage


@pytest.mark.usefixtures('chrome')
class TestElementsPage:
    def test_page(self):
        page = ElementsPage(self.driver)
        page.open()
        page.get_elements_page_categories()
        elements = page.get_elements_page_categories()
        assert len(elements) == 9

    def test_text_box(self):
        page = TextBoxPage(self.driver)
        page.open()
        page.fill_full_name_field('Vasya Pupkin')
        page.fill_email_field('pupkin@gmail.com')
        page.fill_current_address_field('Pupkin`s current addr')
        page.fill_permanent_address_field('Pupkin`s perm addr')
        page.click_submit()
        pass
