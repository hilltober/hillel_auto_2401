# Testing a REST API with Pytest can be done by sending HTTP requests
# to the API and verifying the response. You can use the requests library
# in Python to send HTTP requests and Pytest to write tests
# and verify the responses.
#
# Here's an example of how to test a REST API with Pytest:
import pytest
import requests


@pytest.mark.skip('just synthetic test, that url not real')
def test_get_users():
    response = requests.get("https://api.example.com/users")
    assert response.status_code == 200
    assert response.json()["users"]


@pytest.mark.skip('just synthetic test, that url not real')
def test_get_user():
    response = requests.get("https://api.example.com/users/1")
    assert response.status_code == 200
    assert response.json()["user"]


@pytest.mark.skip('just synthetic test, that url not real')
def test_create_user():
    response = requests.post("https://api.example.com/users", json={
        "name": "John Doe",
        "email": "john.doe@example.com"
    })
    assert response.status_code == 201
    assert response.json()["user"]


@pytest.mark.skip('just synthetic test, that url not real')
def test_update_user():
    response = requests.put("https://api.example.com/users/1", json={
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    })
    assert response.status_code == 200
    assert response.json()["user"]


@pytest.mark.skip('just synthetic test, that url not real')
def test_delete_user():
    response = requests.delete("https://api.example.com/users/1")
    assert response.status_code == 204

# У цьому прикладі бібліотека requests використовується для надсилання
# запитів HTTP до API.
# requests.get використовується для надсилання запитів GET,
# requests.post для надсилання запитів POST,
# requests.put для надсилання запитів PUT,
# requests.delete для надсилання запитів DELETE.

# Атрибут response.status_code використовується для перевірки коду стану HTTP
# відповіді.
# метод response.json використовується для аналізу відповіді JSON.
# Для перевірки того, що відповідь відповідає очікуванням
# використовується оператор assert

# Використовуючи Pytest і бібліотеку requests, можна писати тести
# для REST API простим і зрозумілим способом.
# Ви також можете використовувати Pytest фікстури, щоб налаштовувати
# та відключати ресурси необхідні для тестів, а також для обміну даними
# між тестами.
# Це може допомогти зробити ваші тести більш модульними
# та придатними для повторного використання.
