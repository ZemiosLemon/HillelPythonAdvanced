from flask import Flask
from task_1 import student_param
from task_2 import return_requirements
from task_3 import random_list

app = Flask(__name__)


@app.route('/get_avr_data')
def get_avr_data():
    return f'Средний рост студентов в см: {student_param()[0]} <br> Средний вес студентов в кг: {student_param()[1]}'


@app.route('/requirements')
def get_requirements():
    return return_requirements().replace('\n', '<br>')


@app.route('/random_students')
def random_students():
    return '<br>'.join(random_list())


app.run(debug=True)
