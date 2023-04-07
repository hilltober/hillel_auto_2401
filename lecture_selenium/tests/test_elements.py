import pytest

from lecture_selenium.ElementsPage import ElementsPage


@pytest.mark.usefixtures('chrome')
class TestElementsPage:
    def test_page(self):
        page = ElementsPage(self.driver)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 9
