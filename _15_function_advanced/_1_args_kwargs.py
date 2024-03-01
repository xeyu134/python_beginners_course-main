def add_all(*args):  # Используем, когда надо передать несколько переменных. Тип - turple.
    summary = 0
    for num in args:
        summary += num
    return summary


print(add_all(1, 2, 3))  # Outputs: 6
print(add_all(1, 2, 3, 4, 5))  # Outputs: 15

values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

print(add_all(*values))  # Outputs: 15.
# Важно использовать переменную со звездочкой, чтобы код понял, что это именно переменная, а не значение.
print(add_all(*values, *other_values))  # Outputs: 55


def introduce(**kwargs):  # Это когда надо передать ключи и значения. Тип - словарь
    for key, value in kwargs.items():
        print(key)
        print(value)


introduce(name="John", age=30, city="New York")

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}

introduce(**person)  # Кавычки обязательны. Мы передаем не ключи и значения, а переменную, которая содержит эти данные.


def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)


func_with_all_arguments(
    *[3, 4, 5, 6, 7, 8, 9],
    x=1, y=2,
    **person
)
