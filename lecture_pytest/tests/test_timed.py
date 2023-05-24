import time
import pytest


@pytest.mark.timed
def test_1():
    time.sleep(5)
    pass


@pytest.mark.timed
def test_2():
    time.sleep(5)
    pass


@pytest.mark.timed
def test_3():
    time.sleep(5)
    pass


@pytest.mark.timed
def test_4():
    time.sleep(5)
    pass


@pytest.mark.timed
def test_5():
    time.sleep(5)
    pass
