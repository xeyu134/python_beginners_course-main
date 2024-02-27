'''
Кортеж - неизменяемый список.
'''

user_roles = ("admin", "editor", "viewer")
print(user_roles)  # Outputs: ("admin", "editor", "viewer")

user_roles = ("admin", "editor", "viewer")
print(len(user_roles))  # Outputs: 3

for role in user_roles:
    print(role)

print("admin" in user_roles)  # Outputs: True
print("writer" in user_roles)  # Outputs: False

print(user_roles[1])  # Outputs: "admin"
# user_roles[1] = "author"  # TypeError: 'tuple' object does not support item assignment

not_tuple = ("apple")  # это не кортеж, это строка
print(type(not_tuple))  # Outputs: <class 'str'>

my_tuple = ("admin",)  # а с запятой на конце - кортеж
print(type(my_tuple))  # Outputs: <class 'tuple'>

'''
Распаковка кортежа
'''

user_roles = ("admin", "editor", "viewer")
role_1, role_2, role_3 = user_roles  # кол-во переменных должно быть равно кол-ву элементов,
# иначе не получится распаковать кортеж
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
print(role_3)  # Outputs: "viewer"

user_roles = ["admin", "editor", "viewer"]  # with lists it works too
role_1, role_2, role_3 = user_roles
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
print(role_3)  # Outputs: "viewer"

role_1, role_2, _ = user_roles  # А вот в таком случае получится распоковать 2 элемента
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"

'''
Кортеж используется тогда, когда мы точно знаем, что список не должен изменяться.
Обычно применяется с ф-циями.
'''
