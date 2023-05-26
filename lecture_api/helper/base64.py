import base64


def encode_base64(username: str, password: str) -> str:
    credentials = f'{username}:{password}'
    encoded = base64.b64encode(credentials.encode()).decode()
    return encoded
