from flask import Flask


app = Flask(__name__)

@app.route('/count')
def count():
    return
