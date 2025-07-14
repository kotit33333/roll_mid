from data_base_folder import data_base_connect

def registirion(login, password):
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


def nubmer_to_data_base(login, number):
    connection = data_base_connect.star_connecet_db()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) as count FROM user WHERE login = %s"
            cursor.execute(sql, (login,))
            result = cursor.fetchone()
            cursor.execute("UPDATE `user` SET `row` = CONCAT(`row`, %s) WHERE `login` = %s", (number, login))
            connection.commit()
            return True



