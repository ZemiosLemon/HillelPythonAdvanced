
from flask import Flask
from utils import list2dict


app = Flask(__name__)


@app.route('/get_duration_tracks')
def get_duration_tracks():
    return list2dict()


app.run(debug=True)
