person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}
person.update(additional_person_info)  # метод добавления второго словаря в скобках к первому,
# а также обновляет старые значения на новые.
print(person)  # Outputs: {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}
# Обрати внимание, обновился город

'''
Но есть более удобный способ, чтобы объединить два словаря - |
'''

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}
person = person | additional_person_info
print(person)  # Outputs: {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}
