import psycopg2
import os
from dotenv import load_dotenv


load_dotenv('config.env')


db = os.getenv('DATABASE')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')


def connect_to_database():
    try:
        conn = psycopg2.connect(dbname=db, user=login, password=password, host=host, port=port)
        print('Соединение с базой данных установлено!')
        return conn
    except psycopg2.OperationalError as e:
        print(e)
        print('Ошибка соединения с базой данных!')
        return False
