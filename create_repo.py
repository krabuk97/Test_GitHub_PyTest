import pytest
import requests
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=4)
def test_create_repo(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    body = {"name": "Test_GitHub_PyTest"}
    response = requests.post("https://api.github.com/user/repos", headers=headers, json=body)

    assert response.status_code == 201
    repo_info = response.json()
    assert "name" in repo_info and repo_info["name"] == "Test_GitHub_PyTest"
