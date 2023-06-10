import pytest
import requests
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=5)
def test_update_repo(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    body = {"name": "New_Test_Repo"}

    response_get = requests.get("https://api.github.com/repos/krabuk97/Test_GitHub_PyTest", headers=headers)
    assert response_get.status_code == 200
    repo_info = response_get.json()

    response_patch = requests.patch(repo_info["url"], headers=headers, json=body)
    assert response_patch.status_code == 200

    response_get_updated = requests.get("https://api.github.com/repos/krabuk97/New_Test_Repo", headers=headers)
    assert response_get_updated.status_code == 200
    repo_info_updated = response_get_updated.json()
    assert "name" in repo_info_updated and repo_info_updated["name"] == "New_Test_Repo"
