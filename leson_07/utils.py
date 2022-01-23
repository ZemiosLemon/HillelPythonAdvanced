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


def top_tracks(count):
    sql = 'select TrackId , Quantity , UnitPrice from invoice_items '
    sql_tracks = 'select TrackId , Name from tracks'
    records_info = execute_query(sql)
    records_name = execute_query(sql_tracks)
    name_list = [records_name[i - 1] for i in [i[0] for i in records_info]]
    sort_list = sorted([(name_list[i][1], records_info[i][1] * records_info[i][2])
                        for i in range(len(name_list))], key=lambda x: x[1], reverse=True)
    return sort_list[:count]


def list_rec2html(s_list):
    result = ''
    for i in range(len(s_list)):
        result += f'<br>Название:  "{s_list[i][0]}"  <b>  сумма:  {s_list[i][1]}</b>'
    return result
