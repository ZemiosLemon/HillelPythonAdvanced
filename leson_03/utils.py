import requests


def get_requests(currency):
    currency = currency.upper()
    date = requests.get('https://bitpay.com/api/rates').json()

    for num in date:
        if num['code'] == currency:
            return num['name'], num['rate']
