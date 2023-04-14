import pytest


class TestFixtureTests1:

    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.functional
    def test_1(self):
        print('\nsmoke1')

    @pytest.mark.smoke
    @pytest.mark.negative
    @pytest.mark.functional
    def test_2(self):
        print('\nsmoke2')


class TestFixtureTests2:

    @pytest.mark.regression
    @pytest.mark.positive
    def test_1(self):
        print('\nregr1')

    @pytest.mark.regression
    @pytest.mark.positive
    @pytest.mark.functional
    def test_2(self):
        print('\nregr2')

    @pytest.mark.regression
    @pytest.mark.negative
    def test_3(self):
        print('\nregr3')
