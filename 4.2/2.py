import jwt  # тут используем библиотеку PyJWT

# сукретный ключ , вот это мы должны шифровать и хранить защищенно
SECRET_KEY = "QWERTYZXCVB"
# время жизни токена
ALGORITHM = "HS256"


# в реальности храним только хэши паролей (библиотека passlib) + добавка к паролю
USERS_DATA = [{"username": "admin", "password": "adminpass"}]


# функция для создания JWT токена
def create_jwt_token(data: dict):
    # кодируем токен, передавая в него наш словарь с тем, что мы хотим там разместить
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_user_from_token(token: str):
    try:
        # декодируем токен
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время 'сгорания' и другое, что мы сами туда кладем
        return payload.get("sub")

    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        pass


def get_user(username: str):
    for user in USERS_DATA:
        if user.get("username") == username:
            return user
    return None


# закодируем токен, внеся в него словарь с утверждением о пользователе
token = create_jwt_token({"sub": "admin"})

print(token)

# декодируем токен и излечем из него информацию о юзере, которую мы туда зашили
username = get_user_from_token(token)

print(username)

current_user = get_user(username)

print(current_user)
