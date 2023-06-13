from selene.api import by, be, have, s, ss, browser
from selene.support.shared import config

config.timeout = 6


def test_active_button():
    browser.open('https://demoqa.com/dynamic-properties')
    button = s(by.id('enableAfter'))
    assert button.should(be.enabled)


def test_color_change_button():
    browser.open('https://demoqa.com/dynamic-properties')
    button = s(by.id('colorChange'))
    assert button.should(have.attribute('class').value_containing('danger'))


def test_appears_button():
    browser.open('https://demoqa.com/dynamic-properties')
    button = s(by.id('visibleAfter'))
    assert button.should(be.visible)


def test_all_buttons():
    browser.open('https://demoqa.com/dynamic-properties')
    buttons = ss(by.xpath('//div/button'))
    buttons.wait_until(have.size(3))
    assert buttons[0].should(be.enabled)
    assert buttons[1].should(have.attribute('class').value_containing('danger'))
    assert buttons[2].should(be.visible)
