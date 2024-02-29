def introduce (**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}

introduce(**person)
