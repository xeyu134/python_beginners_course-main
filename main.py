import time, requests

url = 'https://api.binance.com/api/v3/ticker/price'

bitcoin_prices = []
for i in range(30):
    responce = requests.get(url, params = {'symbol': 'BTCUSDT'})
    content = responce.json()  # Забрали контент из запроса и конвертнули в словарь JSON/
    price = float(content['price'])  # Забрали значение по ключу.
    bitcoin_prices.append(price)  # Добавили его в список bitcoin_prices.
    time.sleep(1)  # Создаем задержку в одну секунду.

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))

# Через 30 секунд выдаст результат.
