from flask import Flask

app = Flask(__name__)


@app.route("/avr_data")
def get_avr_data():
    return
