import pytest


class TestFixtures:

    def test_fixtures(self, package_text_fixture):
        text = package_text_fixture + '7'
        assert text == '1234567'
