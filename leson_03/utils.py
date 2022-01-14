import requests

response = requests.get('https://bitpay.com/api/rates').json()

print(response)

