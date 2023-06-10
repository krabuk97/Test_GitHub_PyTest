import pytest
import requests
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=8)
def test_delete_repo(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    repo_name = "New_Test_Repo"
    response = requests.delete(f"https://api.github.com/repos/krabuk97/{repo_name}", headers=headers)

    assert response.status_code == 204
    assert response.content == b''
