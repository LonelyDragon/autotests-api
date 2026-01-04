import httpx

from tools.fakers import fake

BASE_URL = "http://localhost:8000/"

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post(f"{BASE_URL}api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']
print(f'User {user_id} was created')

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post(f"{BASE_URL}api/v1/authentication/login", json=login_payload)
user_token = login_response.json()['token']['accessToken']
print(f"User {user_id} was authenticated.\nBearer token: {user_token}")

auth_user_header = {
    "Authorization": f"Bearer {user_token}"
}

update_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
updated_user_response = httpx.patch(f"{BASE_URL}api/v1/users/{user_id}",
                                    headers=auth_user_header, json=update_payload)
updated_user_data = updated_user_response.json()
print(f"User {user_id} was updated.\nNew email: {updated_user_data['user']['email']}")
