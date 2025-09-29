import httpx

# Проходим аутентификацию
login_payload = {
    "email": "test@test.com",
    "password": "12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

token = login_response_data["token"]["accessToken"]
client = httpx.Client(base_url="http://localhost:8000",
                      timeout=100,
                      headers={"Authorization": f"Bearer {token}"})

response = client.get("/api/v1/users/me")
get_user_me_response_data = response.json()
print('Get user me data:', get_user_me_response_data)