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


# def get_top_tracks():
sql = 'select TrackId , Quantity , UnitPrice from invoice_items '
sql_name = 'select TrackId , Name, UnitPrice from tracks'
records = list(map(list, execute_query(sql)))
records_name = list(map(list, execute_query(sql_name)))
# eeee = [i[0] for i in records]
# print(eeee[:6])
# print(records[:6])
list_name = [records_name[i-1] for i in [i[0] for i in records]]
print(list_name[:6])
print(records[:6])
result = []
for k in range(len(list_name)):
    result += list_name[k][2]* records[k][1]

print(result)
