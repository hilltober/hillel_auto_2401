import pytest
import requests
import json
import pprint


class TestAPI:
    pp = pprint.PrettyPrinter(depth=4)

    @pytest.mark.api
    def test_list_users(self):
        response = requests.get('https://reqres.in/api/users?page=2')
        assert response.status_code == 200
        parsed = json.loads(response.content)
        assert all([
            parsed.get('per_page') == 6,
            'contributions' in parsed.get('support').get('text'),
            'support-heading' in parsed.get('support').get('url'),
            len(parsed.get('data')) == 6,
            all([name.get('first_name') for name in [
                record for record in parsed.get('data')]]),
        ])

    @pytest.mark.api
    def test_single_user(self):
        response = requests.get('https://reqres.in/api/users/2')
        assert response.status_code == 200
        parsed = json.loads(response.content)
        data_success = all([x for x in parsed['data'].values()])
        is_first_name_present = parsed.get('data').get('first_name')
        parsed['data']['first_name'] = ''
        is_check_correct = not parsed.get('data').get('first_name')
        is_avatar_present = requests.get(
            parsed.get('data').get('avatar')).status_code == 200
        assert all([
            data_success, is_first_name_present,
            is_check_correct, is_avatar_present])

    @pytest.mark.api
    def test_single_user_not_found(self):
        response = requests.get('https://reqres.in/api/users/23')
        assert response.status_code == 404
        assert not dict(json.loads(response.content))

    @pytest.mark.api
    def test_list_resource(self):
        response = requests.get('https://reqres.in/api/unknown')
        parsed = json.loads(response.content)
        assert response.status_code == 200
        assert len(parsed.get('data')) == parsed.get('per_page')

    @pytest.mark.api
    def test_single_resource(self):
        response = requests.get(url='https://reqres.in/api/unknown/2')
        parsed = json.loads(response.content)
        assert response.status_code == 200
        assert sorted(
            parsed.get('data').keys()) == sorted(
            ['id', 'name', 'year', 'color', 'pantone_value'])

    @pytest.mark.api
    def test_with_auth(self):
        username = 'postman'
        password = 'password'
        url = 'https://postman-echo.com/basic-auth'
        headers = {
            'Authorization': f'Basic {encode_base64(username, password)}==',
        }
        response = requests.get(url, headers=headers)
        assert json.loads(response.text).get('authenticated')

    @pytest.mark.api
    def test_post_example_1(self):
        url = "https://www.example.com"
        headers = {
            "User-Agent": "MyApp/1.0",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {"key": "value"}
        response = requests.post(url, headers=headers, json=data)
        print(response.text)

    @pytest.mark.api
    def test_post_example_2(self):
        url = 'https://reqres.in/api/users'
        data = {'name': 'morpheus',
                'job': 'leader'}
        response = requests.post(url, json=data)
        assert json.loads(response.text).get('id')
        print(response.text)


def encode_base64(username: str, password: str) -> str:
    import base64
    credentials = f'{username}:{password}'
    encoded = base64.b64encode(credentials.encode()).decode()
    return encoded


def decode_base64(string: str) -> str:
    import base64
    decoded_bytes = base64.b64decode(string)
    decoded_string = decoded_bytes.decode()
    return decoded_string
