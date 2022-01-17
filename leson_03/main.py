from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from utils import get_requests

app = Flask(__name__)


@app.route('/')
@use_kwargs(
    {
        'currency': fields.Str(
            required=False,
            missing='USD',
            validate=[validate.Length(equal=3)]
        )
    },
    location='query'
)
def get_avr_data(currency):
    result = get_requests(currency)
    return f'Rate of bitcoin to the {result[0]} is equal to  {result[1]}'


app.run(debug=True)
