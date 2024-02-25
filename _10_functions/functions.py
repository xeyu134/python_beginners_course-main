'''
Функция - блок кода для многократного повторения

Есть постоянные, такие как print(), а можно написать свои.
'''

'''
Пример: расчет среднего значения чисел в списке
'''
numbers_1 = [1, 2, 3, 4, 5]
average_1 = sum(numbers_1) / len(numbers_1)
print(average_1)  # Outputs: 3.0

numbers_2 = [6, 7, 8, 9, 10]
average_2 = sum(numbers_2) / len(numbers_2)
print(average_2)  # Outputs: 8.0

'''
Проблема кода выше в том, что мы делаем одно и то же действие для первого списка,
а потом для ворого. 
Но есть правило в Python (да и вообще в программировании): don't repeat yourself (DRY).
Поэтому, повторяющее действие лучше записать в функцию
'''
def find_average(numbers):  # find_average - осмысленное название функции. 
# Numbers - новая созданная осмысленная переменная, куда будут подставляться значения
    average = sum(numbers) / len(numbers)  # сделали вычисление
    return average  # надо вернуть результат ф-ции. Это ОБЯЗАТЕЛЬНО!
    # Иначе по умолчанию возвращется ничего, т.е. None.


average_1 = find_average(numbers_1)  # в numbers подставляем значения numbers_1
average_2 = find_average(numbers_2)
print(average_1, average_2)  # 3.0 8.0

'''
Пример: счет гласных букв
'''
def count_vowels(string):
    vowels = 'aeiouyAEIOUY'  # Хоть это и str, но это также список всех гласных букв.
    # Регистр ВАЖЕН!
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello, World!"))  # Outputs: 3
print(count_vowels("Python is a very powerful language."))  # Outputs: 11

'''
Пример: заглушка
'''
def nothing():
    print("This function does nothing.")
    # В данном случае все равно выведет строку. Поэтому надо использовать вариант ниже


def nothing():
    pass
    # Это нужно, когда мы знаем, что ф-ция будет, но ее еще не написали.
    # Зато в коде место под нее выделили.


my_variable = nothing()
print(my_variable)  # Outputs: None
print(nothing())  # Outputs: None

'''
Пример: несколько аргументов. Дата.
'''
def format_date(day, month):
    return f"The date is {day} of {month}."


print(format_date(15, "October"))  # Outputs: The date is 15 of October.
print(format_date("January", 1))  # Outputs: "The date is January of 1."
# Соблюдение порядка аргументов ВАЖНА (по смыслу)!

'''
Чтобы не перепутать аргументы, можно прописать типы для аргументов
'''
def format_date(*, day: int, month: str) -> str:
    # В day заходит только число, а в month - только строка.
    # А сама ф-ция должна выдать str. Это больше для другого прогера, а не интепретатора
    # * - обязательное наличие day и month. Правило: явное лучше неявного.
    # Без нее аргументы можно передавать просто как (15,"October"),
    # а с ней: обязательно (day=15, month="October").
    return f"The date is {day} of {month}."


print(format_date(day=15, month="October"))  # Outputs: The date is 15 of October.
# Выше мы сделали проверку аргументов ф-ции. Своего рода гигиена.


def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    # "Hello" - дефотный аргумент, он может замениться.
    return f"{greeting}, {name}"


print(custom_greeting(name="John"))  # Outputs: Hello, John
# Так как для greeting уже есть дефотный аргумент, его прописывать не надо.
print(custom_greeting(name="John", greeting="Good morning"))  # Outputs: Good morning, John
