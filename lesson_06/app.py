
from flask import Flask
from utils import duration_tracks


app = Flask(__name__)


@app.route('/get_duration_tracks')
def get_duration_tracks():
    return duration_tracks()


app.run(debug=True)
