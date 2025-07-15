from data_base_folder import data_base_connect
import time

def register_user(login, password):
    connection = data_base_connect.star_connecet_db()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) as count FROM user WHERE login = %s"
            cursor.execute(sql, (login,))
            result = cursor.fetchone()
            if result['count'] == 0:

                cursor.execute("INSERT INTO user (login, password) VALUES (%s, %s)", (login, password))
                connection.commit()
                return True
            else:
                return False


def login(login, password)-> tuple[bool, str]:
    connection = data_base_connect.star_connecet_db()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT password FROM user WHERE login = %s", (login,))
            result_password = cursor.fetchone()
            connection.commit()
            if password == result_password['password']:
                return True, 'Успешный вход'
            return False, 'Невеерный логин или пароль'


def add_choice_to_db(login, choice, is_correct):
    connection = data_base_connect.star_connecet_db()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO user_choices (login, choice, is_correct) VALUES (%s, %s, %s)"
                cursor.execute(sql, (login, choice, is_correct))
            connection.commit()
        return True
    except:
        return False


def get_choices(login):
    connection = data_base_connect.star_connecet_db()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT choice FROM user_choices WHERE login = %s"
            cursor.execute(sql, (login,))
            results = cursor.fetchall()

    choices = [row["choice"] for row in results]
    return choices


