import pytest
import requests
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=1)

def test_authentication(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://api.github.com/user", headers=headers)

    assert response.status_code == 200
    assert "login" in response.json()
    assert "name" in response.json()
    assert "email" in response.json()