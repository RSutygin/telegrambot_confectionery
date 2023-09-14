import os
from dotenv import load_dotenv

load_dotenv('config.env')

table_ord = os.getenv('TABLE_ORD')
table_pr = os.getenv('TABLE_PR')


def add_id(conn, new_id):
    with conn.cursor() as cursor:
        cursor.execute(
            f'DO $$ '
            f'BEGIN '
            f'IF NOT EXISTS (SELECT * FROM {table_ord} WHERE id = {new_id}) then '
            f'INSERT INTO {table_ord} (id) VALUES ({new_id}); '
            f'END IF; '
            f'END $$'
        )
        conn.commit()
        cursor.execute(
            f'SELECT name '
            f'FROM {table_ord} '
            f'WHERE id = {new_id}'
        )
        name = cursor.fetchall()
        if name[0][0] is None:
            return True
        else:
            return False


def update_dessert(conn, chat_id, dessert):
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE {table_ord} SET dessert = '{dessert}' "
            f"WHERE id = {chat_id}"
        )
        conn.commit()


def update_count(conn, chat_id, count):
    with conn.cursor() as cursor:
        cursor.execute(
            f'UPDATE {table_ord} SET count = {count} '
            f'WHERE id = {chat_id}'
        )
        conn.commit()


def update_messanger(conn, chat_id, messenger):
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE {table_ord} SET messenger = '{messenger}' "
            f"WHERE id = {chat_id}"
        )
        conn.commit()


def update_price(conn, chat_id):
    with conn.cursor() as cursor:
        cursor.execute(
            f'UPDATE {table_ord} SET price = {table_ord}.count * '
            f'(SELECT price FROM {table_pr} where dessert = '
            f'(SELECT dessert FROM {table_ord} WHERE id = {chat_id})) '
            f'WHERE id = {chat_id}'
        )
        conn.commit()


def get_price(conn, chat_id):
    with conn.cursor() as cursor:
        cursor.execute(
            f'SELECT price '
            f'FROM {table_ord} '
            f'WHERE id = {chat_id}'
        )
        return cursor.fetchall()


def update_number_or_username(conn, chat_id, noru):
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE {table_ord} SET number_or_username = '{noru}' "
            f"WHERE id = {chat_id}"
        )
        conn.commit()


def get_all(conn, chat_id):
    with conn.cursor() as cursor:
        cursor.execute(
            f'SELECT * '
            f'FROM {table_ord} '
            f'WHERE id = {chat_id}'
        )
        return cursor.fetchall()


def update_name(conn, chat_id, name):
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE {table_ord} SET name = '{name}' "
            f"WHERE id = {chat_id}"
        )
        conn.commit()


def check_messenger_and_number(conn, chat_id):
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT messenger, number_or_username "
            f"FROM {table_ord} "
            f"WHERE id = {chat_id}"
        )
        received = cursor.fetchall()
        if received[0][0] is None and received[0][1] is None:
            return False
        else:
            return True


def get_all_id(conn):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id"
            "FROM orders"
        )
        return cursor.fetchall()


def get_name(conn, chat_id):
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT name "
            f"FROM {table_ord} "
            f"WHERE id = {chat_id}"
        )
        return cursor.fetchall()


def update_date(conn, chat_id, date):
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE {table_ord} SET date = '{date}' "
            f"WHERE id = {chat_id}"
        )
        conn.commit()


def update_decor(conn, chat_id, decor):
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE {table_ord} SET decor = '{decor}' "
            f"WHERE id = {chat_id}"
        )
        conn.commit()


def get_messenger_and_number(conn, chat_id):
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT messenger, number_or_username "
            f"FROM {table_ord} "
            f"WHERE id = {chat_id}"
        )
        return cursor.fetchall()