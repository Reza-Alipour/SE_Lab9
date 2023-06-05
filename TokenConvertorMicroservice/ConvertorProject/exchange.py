import requests
from django.http import JsonResponse


def convert_price(request):
    from_token = request.GET['from_token']
    to_token = request.GET['to_token']
    amount = float(request.GET['amount'])
    print("hello world")
    price_microservice_addr = 'http://PriceService:8001'
    from_token_price = float(requests.get(f'{price_microservice_addr}/price?token={from_token}').text)
    to_token_price = float(requests.get(f'{price_microservice_addr}/price?token={to_token}').text)
    return JsonResponse({
        "from_token_usd_price": from_token_price,
        "to_token_usd_price": to_token_price,
        "receive_amount": from_token_price * amount / to_token_price
    })
