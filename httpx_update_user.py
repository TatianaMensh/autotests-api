import httpx

from httpx_get_user_me import access_token
from tools.faker import get_random_email

# Создание пользователя
user_payload = {
  "email": get_random_email(),
  "password": "125638",
  "lastName": "testLast",
  "firstName": "testFirst",
  "middleName": "testMiddle"
}

response_create_user = httpx.post("http://localhost:8000/api/v1/users", json=user_payload)
response_create_user_data = response_create_user.json()
print(f"Создан пользователь с данными: {response_create_user_data}\n"
      f"Статус код ответа от сервера: {response_create_user.status_code}")

# Авторизация пользователя
response_auth_user = httpx.post("http://localhost:8000/api/v1/authentication/login",
                                json={"email": user_payload["email"], "password": user_payload["password"]})
response_auth_user_data = response_auth_user.json()
print(f"Токен для этого пользователя: {response_auth_user_data}\n"
      f"Статус код ответа от сервера: {response_auth_user.status_code}")

# Изменение данных пользователя
new_data_user = {
    "email": get_random_email(),
    "lastName": "test_2Last",
    "firstName": "test_2First",
    "middleName": "test_2Middle"
}
id_user = response_create_user_data["user"]["id"]
token = response_auth_user_data["token"]["accessToken"]
response_update_user = httpx.patch(f"http://localhost:8000/api/v1/users/{id_user}",json=new_data_user,
                                   headers={"Authorization": f"Bearer {token}"})
print(f"Обновление пользователя с id={id_user}, новые данные: {response_update_user.json()}\n"
      f"Статус код ответа от сервера: {response_update_user.status_code}")