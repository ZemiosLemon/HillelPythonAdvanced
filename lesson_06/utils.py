import os.path
import sqlite3
import datetime


def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'example.sqlite3')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    records = cursor.fetchall()
    return records


def duration_tracks():
    sql = 'select "GenreId", "Milliseconds" from tracks '
    sql_gen = 'select "Name" from genres'
    records = execute_query(sql)
    records_genre = execute_query(sql_gen)
    duration_list = []
    for j in range(1, len(records_genre) + 1):
        duration_list.append(sum([i[1] for i in records if i[0] == j]))
    return records_genre, duration_list


def time_format():
    time_list = duration_tracks()[1]
    return [str(datetime.timedelta(milliseconds=i)) for i in time_list]


def list2dict():
    return dict(zip(map(str, duration_tracks()[0]), time_format()))
