import requests


# Basic authentication
def test_basic_auth():
    response = requests.get('https://api.example.com/protected',
                            auth=('username', 'password'))
    assert response.status_code == 200


# Token-based authentication
def test_token_auth():
    headers = {'Authorization': 'Bearer <token>'}
    response = requests.get('https://api.example.com/protected',
                            headers=headers)
    assert response.status_code == 200


# OAuth2 authentication
def test_oauth2_auth():
    access_token = '<access_token>'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('https://api.example.com/protected',
                            headers=headers)
    assert response.status_code == 200


def test_clean():
    pass
# У цих прикладах бібліотека запитів використовується для надсилання запиту GET
# до кінцевої точки API https://api.example.com/protected.
# Тести перевіряють, що API повертає код статусу 200 OK
# (вказує на успішне виконання запиту).

# У першому прикладі використовується базова автентифікація,
# з параметром auth, що містить ім’я користувача та пароль.

# У другому прикладі використовується автентифікація на основі токенів,
# із заголовком авторизації, встановленим на носій <токен>.

# У третьому прикладі використовується автентифікація OAuth2,
# із заголовком авторизації, встановленим на Bearer <access_token>.


# Зверніть увагу, що в цих прикладах фактичні облікові дані
# та маркери автентифікації було замінено заповнювачами. У реальному сценарії
# ви отримаєте ці значення через потік автентифікації або з безпечного
# файлу конфігурації.
