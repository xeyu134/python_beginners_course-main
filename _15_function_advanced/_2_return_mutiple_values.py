# На входе отдаем словарь и какие-нибудь переменные.
# Ф-ция будет выдавать кортеж, куда входит словарь и bool.
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        # Забираем значение из старого словаря по ключу key, и сравниваем с value из kwargs
        if old_dict.get(key) != value:
            old_dict[key] = value  # Если такого key нету, то он добавляется, как и его значение.
            is_modified = True

    return old_dict, is_modified


product = {'id': 1, 'name': 'Laptop', 'price': 999.99}

structure = modify_dict(old_dict=product, in_stock=True)
# in_stock=True конвертнется в словарь, где первое - это ключ, а второе - значение.
# Так как такого ключа нет, то он добавиться в словарь и его стоковое значение.
print(type(structure))
print(structure)

# Так как ф-ция отдает два значения, то их можно сортировать по двум переменным.
product, was_modified = modify_dict(old_dict=product, in_stock=True)
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: True

product, was_modified = modify_dict(old_dict=product, id=1, name="Laptop")
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: False. Измений не было.