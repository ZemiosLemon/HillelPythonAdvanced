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


def count_rec2html():
    return f'<p> Количество треков в таблице "tracks": {tracks_count()}'


def tracks_count():
    sql = 'select "TrackId" from tracks'
    records = execute_query(sql)
    return len(records)


print(tracks_count())
