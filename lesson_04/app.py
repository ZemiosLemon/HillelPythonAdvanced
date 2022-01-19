from flask import Flask
from db import execute_query
from formater import list_rec2html_br

app = Flask(__name__)


@app.route('/unique_name')
def get_unique_name():
    sql = 'select "FirstName" from customers'
    records = execute_query(sql)
    result = [num for num in records]
    unique_list = []
    for i in result:
        if i not in unique_list:
            unique_list.append(i)
    return list_rec2html_br(unique_list)


app.run(debug=True)
