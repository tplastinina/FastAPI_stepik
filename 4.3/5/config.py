# Этот файл будет содержать конфигурации, такие как секретный ключ и алгоритм:

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

USER_DATA = {
    "admin": {"username": "admin", "password": "adminpass", "role": "admin"},
    "user": {"username": "user", "password": "userpass", "role": "user"},
}  # в реальной БД мы храним только ХЭШИ паролей (можете прочитать про библиотеку, к примеру, 'passlib') + соль (известная только нам добавка к паролю)
