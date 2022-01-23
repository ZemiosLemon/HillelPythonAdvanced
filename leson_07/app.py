from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs
from  utils import top_tracks, list_rec2html


app = Flask(__name__)


@app.route('/top_tracks')
@use_kwargs(
    {
        'count': fields.Int(
            missing=None,
            required=False

        )
    },
    location='query'
)


def get_top_tracks(count):
    return list_rec2html(top_tracks(count))


app.run(debug=True)
