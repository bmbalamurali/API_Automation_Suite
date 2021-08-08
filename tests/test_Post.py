import pytest
import requests
from config import *
from data.testdata import *

error = []


@pytest.mark.Post
def test_create_new_user():
    response = requests.post(base_url + post_create_user, data=create_data_pl)
    assert response.status_code == 201
    assert (response.json()['job'] == 'leader')


@pytest.mark.Post
def test_create_new_user1():
    response = requests.post(base_url + post_create_user, data=create_data_pl1)
    assert response.status_code == 201
    assert (response.json()['name'] == 'Bala')


@pytest.mark.Post
def test_register_success():
    response = requests.post(base_url + post_register_success, data=register_user)
    assert response.status_code == 200
    assert (response.json()['id'] == 4)


@pytest.mark.Post
def test_register_invalid_success():
    response = requests.post(base_url + post_register_success, data=register_invaliduser)
    if response.json()['error'] == "Missing password":
        error.append("Missing password")
    if response.json()['error'] == "Missing email or username":
        error.append("Missing email or username")


@pytest.mark.Post
def test_login_user_success():
    response = requests.post(base_url + post_login_user, data=login_user_success)
    assert response.status_code == 200
    assert (response.json()['token'] == 'QpwL5tke4Pnpja7X4')


@pytest.mark.Post
def test_login_user_invalid_success():
    response = requests.post(base_url + post_login_user, data=login_user_unsuccess)
    if response.json()['error'] == "Missing password":
        error.append("Missing password")
    if response.json()['error'] == "Missing email or username":
        error.append("Missing email or username")
