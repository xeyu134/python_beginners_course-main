import json
'''
JSON - это как csv, для укомплектации таблиц, только данных. Упаковывает ее в одну строку.
Импортируется в стандартную библиотеку.
'''
book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
}

# convert into JSON:
json_string = json.dumps(book)  # Укомплектовываем данные.
print(type(json_string))  # Тип str
print(json_string)  # Outputs: {"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"}

json_string = '{"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"}'
book = json.loads(json_string)  # Распаковка
print(type(book))  # Тип словарь
print(book)  # Outputs: {'title': '1984', 'author': 'George Orwell', 'isbn': '978-0451524935', 'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'}

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
    'count': 30,  # можно упаковать еще и int и другие типы
    'genres': ['dystopia'],
}

json_string = json.dumps(book)
print(type(json_string))
print(json_string)  # Outputs: {"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "count": 30, "genres": ["dystopia"]}