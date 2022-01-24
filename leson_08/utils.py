import os.path
import sqlite3


def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'example.sqlite3')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    records = cursor.fetchall()
    return records


def list_rec2html(s_list):
    result = ''
    for i in range(len(s_list)):
        result += f'<br>Название:  "{s_list[i][0]}"  <b>  сумма:  {s_list[i][1]}</b>'
    return result
