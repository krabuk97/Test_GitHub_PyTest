import pytest
import requests
from dat import token_git

@pytest.fixture
def access_token():
    token = token_git
    return token

@pytest.mark.run(order=7)
def test_delete_test_file(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    filename = "tst.txt"

    response_delete = requests.delete(f"https://api.github.com/repos/krabuk97/New_Test_Repo/contents/{filename}", headers=headers)
    assert response_delete.status_code == 200
