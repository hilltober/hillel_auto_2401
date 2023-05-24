import pickle
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_cookies(chrome):
    driver = chrome
    # Відкриваємо файл збережених cookies
    with open('./cookies.pkl', 'rb') as file:
        cookies = pickle.load(file)
    # Додаємо cookies до веб-драйвера
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get('https://rozetka.com.ua/ua/')
    user_button = driver.find_element(By.XPATH, '(//button[contains(@class, "header__button")])[2]')
    user_button.click()
    _ = driver.find_element(By.CSS_SELECTOR, 'div.modal__holder')
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    password_field = driver.find_element(By.CSS_SELECTOR, 'input#auth_pass')
    email_field.send_keys('hilltober@gmail.com')
    password_field.send_keys('Gfhjkm123')
    remember_checkbox = driver.find_element(By.CSS_SELECTOR, 'label[for="remember_me"]')
    remember_checkbox.click()
    submit_button = driver.find_element(By.XPATH, '//button[contains(@class, "auth-modal__submit")]')
    submit_button.click()
    pass
