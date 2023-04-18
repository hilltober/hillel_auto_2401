import time

from selenium.webdriver.remote.webelement import WebElement


def wait_element_to_be_enabled(element: WebElement, timeout: int) -> bool:
    """
    :param element: WebElement from function caller
    :param timeout: Max time to wait for element to be enabled
    :return: True if element is enabled
    """
    end_time = time.monotonic() + timeout
    while time.monotonic() <= end_time:
        if element.is_enabled():
            return True
        else:
            time.sleep(0.1)
    raise TimeoutError(f'Element is not enabled after {timeout} seconds')
