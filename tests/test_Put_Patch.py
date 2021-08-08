import requests
from config import *
from data.testdata import *
import pytest


@pytest.mark.PutPatch
def test_update_user():
    response = requests.put(base_url + put_update_user, data=update_user)
    assert response.status_code == 200
    assert (response.json()['job'] == 'Chennai')


@pytest.mark.PutPatch
def test_update_user_property():
    response = requests.patch(base_url + patch_update_user, data=patch_user)
    assert response.status_code == 200
    assert (response.json()['job'] == 'Automation')
