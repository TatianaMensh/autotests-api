import httpx

# from tools.faker import get_random_email

# Создаем пользователя
user_payload = {
    "email": "test@test.ru",
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
post_user = httpx.post("http://localhost:8000/api/v1/users", json=user_payload)
user_data = post_user.json()
print(f"Create user data: {user_data}")

# Аутентификация пользователя
user_data = {
  "email": user_payload["email"],
  "password": user_payload["password"]
}
auth_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user_data)
token = auth_user.json()
print(f"Token: {token}")

# Загрузка файла
headers_file = {"Authorization": f"Bearer {token['token']['accessToken']}"}
data_file = {
    "filename": "image.png",
    "directory": "courses"
}
file = {"upload_file": open("./testdata/files/image.png", "rb")}
upload_file = httpx.post("http://localhost:8000/api/v1/files",
                         data=data_file,
                         files=file,
                         headers=headers_file)
upload_file_data = upload_file.json()
print(f"Create file data: {upload_file_data}")



