import mysql.connector
from decouple import config

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host = config('MYSQL_HOST'),
            user = config('MYSQL_USER'),
            password = config('MYSQL_PASSWORD'),
            database = config('MYSQL_DATABASE')
        )
        return conexion
    except mysql.connector.Error as error:
        raise error
    