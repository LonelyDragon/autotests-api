import httpx

payload = {
    "email": "user@mail.com",
    "password": "123456"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

print("Status Code:", login_response.status_code)
print("Login response:", login_response_data)

access_token = login_response_data["token"]["accessToken"]
headers = {"Authorization": f"Bearer {access_token}"}

user_info_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Status code:", user_info_response.status_code)
print(f"Get user me response:", user_info_response.json())
