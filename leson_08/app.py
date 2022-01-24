from flask import Flask
from utils import execute_query, list_rec2html
from webargs import fields
from webargs.flaskparser import use_kwargs


app = Flask(__name__)


@app.route('/genres')
def genres_duration():
    sql = 'select g.Name, SUM(t.Milliseconds)/1000 /60 from tracks as t ' \
          'join genres as g on t.GenreId = g.GenreId group by g.GenreId;'

    records = execute_query(sql)
    return list_rec2html(records)


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
    sql = 'select t.Name, SUM(i.Quantity*i.UnitPrice) as revenue from tracks as t ' \
          'join invoice_items as i on t.TrackId = i.TrackId group by t.TrackId order by revenue desc;'
    records = execute_query(sql)[:count]
    return list_rec2html(records)


app.run(debug=True)
