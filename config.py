import random

# base url ***************************

base_url = 'https://reqres.in/'

# *************************************

# random number generation ***************************

list_user_page = random.randint(1, 12)
single_user_not_found = random.randint(13, 23)
single_resource_not_found = random.randint(13, 23)
update_user = random.randint(1, 12)
patch_user = random.randint(1, 12)
delete_user = random.randint(1, 12)

# *************************************

# GET METHOD REQUEST ******************

get_list_user = f'api/users?page={list_user_page}'
get_single_user = 'api/users/5'
get_single_user_not_found = f'api/users/{single_user_not_found}'
get_list_resources = 'api/unknown'
get_single_resource = 'api/unknown/2'
get_single_resource_not_found = f'api/unknown/{single_resource_not_found}'
get_delay_response = 'api/users?delay=3'
# *************************************

# POST METHOD REQUEST******************

post_create_user = 'api/users'
post_register_success = 'api/register'
post_login_user = 'api/login'

# *************************************

# PUT METHOD REQUEST******************

put_update_user = f'api/users/{update_user}'

# *************************************

# PUT METHOD REQUEST******************

patch_update_user = f'api/users/{patch_user}'

# *************************************

# DELETE METHOD REQUEST******************

delete_user = f'api/users/{delete_user}'

# *************************************
