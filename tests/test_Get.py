import requests
from config import *
from assertpy.assertpy import assert_that
import pytest


@pytest.mark.Get
def test_get_list_user():
    response = requests.get(base_url + get_list_user)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_text = response.json()
    assert_that(response_text).is_not_equal_to('')


@pytest.mark.Get
def test_get_single_user():
    response = requests.get(base_url + get_single_user)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_text = response.json()
    assert_that(response_text["data"]["first_name"]).contains("Charles")


@pytest.mark.Get
def test_get_single_user_not_found():
    response = requests.get(base_url + get_single_user_not_found)
    assert_that(response.status_code).is_equal_to(404)
    response_text = response.json()
    assert_that(response_text).is_equal_to({})


@pytest.mark.Get
def test_get_list_resources():
    response = requests.get(base_url + get_list_resources)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_text = response.json()
    assert_that(response_text).is_not_equal_to('')


@pytest.mark.Get
def test_get_single_resource():
    response = requests.get(base_url + get_single_resource)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_text = response.json()
    assert_that(response_text["data"]["name"]).contains("fuchsia rose")


@pytest.mark.Get
def test_get_single_resource_not_found():
    response = requests.get(base_url + get_single_resource_not_found)
    assert_that(response.status_code).is_equal_to(404)
    response_text = response.json()
    assert_that(response_text).is_equal_to({})


@pytest.mark.Get
def test_get_delay_response():
    response = requests.get(base_url + get_delay_response, timeout=5)
    if response.status_code == 200:
        assert True
    else:
        assert False
