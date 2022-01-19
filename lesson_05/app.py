from flask import Flask
from utils import count_rec2html


app = Flask(__name__)


@app.route('/tracks_count')
def get_tracks_count():
    return count_rec2html()


app.run(debug=True)
