import re


def is_valid_login(login: str) -> bool:
    """
    Логин может содержать только латинские буквы и цифры, от 3 до 20 символов.
    """
    return bool(re.fullmatch(r"[a-zA-Z0-9]{3,20}", login))


def register_user(login: str, password: str, password_confirm: str) -> tuple[bool, str]:
    """
    Проверка регистрации:
    - логин корректный (без спец. символов)
    - пароли совпадают
    - поля не пустые
    Возвращает (успех, сообщение)
    """
    if not login or not password or not password_confirm:
        return False, "Все поля должны быть заполнены."


    if not is_valid_login(login):
        return False, "Логин может содержать только латинские буквы и цифры (3-20 символов)."

    if password != password_confirm:
        return False, "Пароли не совпадают."
    return True, "Регистрация прошла успешно."


def login_user(login: str, password: str) -> tuple[bool, str]:

    if not login or not password:
        return False, "Все поля должны быть заполнены."

    return True, "Регистрация прошла успешно."