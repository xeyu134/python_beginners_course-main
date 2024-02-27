'''
Словари - набор ключей-значений. Ключи - типо переменная
'''

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}
person["job"] = "Engineer"  # добавили в словарь ноый ключ и его значение
print(person)  # Outputs: {'name': 'John', 'age': 40, 'city': 'New York', 'job': 'Engineer'}

person = {}  # or person = dict(). Тут мы создали пустой словарь.
# А потом добавляем туда ключи и значения.
person["name"] = "John"
person["age"] = 30
person["city"] = "New York"
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Outputs: 'John'
print(person["country"])  # KeyError: 'country'. Чтобы не получить ошибку,
# рекомендуется использовать метод get()
print(person.get("name"))  # Outputs: 'John'
print(person.get("country"))  # Outputs: None
print(person.get("country", "USA"))  # Outputs: USA. 
# Второй параметр задает дефотное значение. Это один из спрособов добавить новый ключ и значение.
print(person.get("name", "Jack"))  # Outputs: John. Но если такой ключ уже есть с значением, то подмены не будет.
