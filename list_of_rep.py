import pytest
import requests
import json
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=3)
def test_list_of_repo(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://api.github.com/user/repos", headers=headers)

    assert response.status_code == 200
    list_repo = response.json()
    assert len(list_repo) > 0

    with open("list.txt", "w") as f:
        json.dump(list_repo, f, indent=4)
