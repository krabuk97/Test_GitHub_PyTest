import pytest
import requests
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=2)

def test_get_user_info(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://api.github.com/user", headers=headers)

    assert response.status_code == 200
    user_info = response.json()
    assert "login" in user_info
    assert "name" in user_info
    assert "email" in user_info
    assert "followers" in user_info
    assert "public_repos" in user_info

    print(user_info)

