import requests
from config import *
from assertpy.assertpy import assert_that
from data.testdata import *
import json

# response = requests.get(base_url+get_single_user_not_found)
# # assert_that(response.status_code).is_equal_to(requests.codes.ok)
# response_text = response.json()
# #first_name = [name['fname'] for name in response_text]
# #assert_that(response_text).contains('Charles')
#
# for name in response_text:
#     print(name[0])
#
# print(response_text)
# print(response.status_code)
# # print(response_text["data"]["email"])

response = requests.delete(base_url+delete_user)
print(response)
print(type(response))
# print(response.json())
# print(response.elapsed.total_seconds())



