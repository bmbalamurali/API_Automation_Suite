import requests
from config import *
import pytest

@pytest.mark.Delete
def test_delete_user():
    response = requests.delete(base_url+delete_user)
    assert response.status_code == 204