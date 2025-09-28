import httpx

# данные пользователя для запросов
login_payload = {
    "email": "test@test.com",
    "password": "12345"
}

# запрос на получение токена для пользователя
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
# записываем полученный токен из запроса в переменную для дальнейшего использования
access_token = login_response_data["token"]["accessToken"]
# вывод ответа от сервера - получение токена
print(f"Получен токен: {login_response_data}")
print(f"Статус код ответа: {login_response.status_code}")

# запрос на получение информации о пользователе, используя токен
current_user = httpx.get("http://localhost:8000/api/v1/users/me",
                         headers={"Authorization": f"Bearer {access_token}"})
# вывод ответа от сервера - получение информации о пользователе
print(f"Получена информация о пользователе: {current_user.json()}")
print(f"Статус код ответа: {current_user.status_code}")




