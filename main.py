import requests  # импортировали библиотеку requests для получения ответа из других ресурсов.

url = 'https://api.binance.com/api/v3/ticker/price'

# Передаем адрес получения данных, и какие параметры нам нужны
responce = requests.get(url, params={'symbol': 'BTCUSDT'})

content = responce.content

print(content)
print(type(content))
'''
Outputs:
b'{\n  "code": 0,\n  "msg": "Service unavailable from a restricted location according to \'b. Eligibility\' in https://www.binance.com/en/terms. Please contact customer service if you believe you received this message in error."\n}'
<class 'bytes'>

Ошибка из-за того, что сервера Replit в USA, а там нельзя делать такие запросы.
В целом, на выходе должно быть следующее:

'''

content_2 = responce.json()  # конвертируем полученные данные в JSON.
# Его тип - это словарь. А значит можно достать значение по ключу.
price = content_2['price']  # получим значение, но это значение в JSON имеет тип str.
price = float(content_2['price'])  # Поэтому лучше сразу конвертнуть в float.

print(price)

