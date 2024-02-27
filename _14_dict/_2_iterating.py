'''
Интерация словаря. Типо распаковка ключей и значений.
'''

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for item in person:
  print(item)  # Выдаст только ключи столбцом.
  print(person[item])  # Выдаст значения. Но такой способ не рекомендуется

for item in person.items():  # Рекомендуется использовать этот метод
    print(item)  # Outputs: ('name', 'John')
    print(type(item))  # Outputs: <class 'tuple'>

for key, value in person.items():  # Т.к. item состоит их ключа и значения,
    # то лучше сразу дзадать для них переменные.
    print(key)
    print(value)

for items in person.items():
    key, value = items  # А можно еще вот так распаковать items
    print(key)
    print(value)

for key in person.keys():  # Специальный метод для ключей
    print(key)  # Выдаст только ключи словаря

for value in person.values():  # Специальный метод для значений
    print(value)  # Выдаст только значения словаря
