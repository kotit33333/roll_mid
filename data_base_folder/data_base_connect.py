from secret_folder import secret
import pymysql

def star_connecet_db():
    connection = pymysql.connect(
        host=secret.host,
        port=secret.port,
        user=secret.user,
        password=secret.password,
        database=secret.database,
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection
