import requests
from django.http import HttpResponse


def get_price(request):
    token = request.GET['token']
    headers = {
        'X-CoinAPI-Key': '0823B72E-709A-409F-A89F-04233D94F164'
    }
    resp = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{token}/USD', headers=headers)
    rate = resp.json()['rate']
    return HttpResponse(rate)
