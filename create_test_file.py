import pytest
import requests
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=6)
def test_create_test_file(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    body = {
        "message": "Add new file",
        "content": "dGVzdA=="
    }
    response = requests.put("https://api.github.com/repos/krabuk97/New_Test_Repo/contents/tst.txt", headers=headers, json=body)

    assert response.status_code == 201
    assert "tst.txt" in response.json()["content"]["name"]
