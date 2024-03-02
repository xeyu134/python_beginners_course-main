import requests  # Импортировали библиотеку requests для получения ответа из других ресурсов.

# Передаем адрес получения данных, и какие параметры нам нужны
response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
content = response.content
print(content)
print(type(content))
'''
Outputs:
b'{\n  "code": 0,\n  "msg": "Service unavailable from a restricted location according to \'b. Eligibility\' in https://www.binance.com/en/terms. Please contact customer service if you believe you received this message in error."\n}'
<class 'bytes'>

Ошибка из-за того, что сервера Replit в USA, а там нельзя делать такие запросы.
В целом, на выходе должно быть следующее:
'''
price_object = response.json()  # конвертируем полученные данные в JSON.
# Его тип - это словарь. А значит можно достать значение по ключу.
price = float(price_object['price'])  # Получим значение, но это значение в JSON имеет тип str.
# Поэтому лучше сразу конвертнуть в float.
print(price)

import time

bitcoin_prices = []
for i in range(30):
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    price = float(response.json()["price"])
    price = round(price, 2)
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))
