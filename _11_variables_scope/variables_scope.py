'''
Область видимости переменных
'''

def my_function():
    local_var = "I'm a local variable"  # Существует только внутри ф-ции
    print(local_var)


my_function()  # Outputs: "I'm a local variable"
# print(local_var)  # This will raise an error because local_var is not defined outside the function

'''
Пример плохого, но рабочего варианта
'''

for i in range(3):
    print(i)

print(i)  # Outputs: 2, but it's bad to use it after the loop

'''
Пример хороший
'''

global_var = "I'm a global variable"


def my_function():
    print(global_var)  # This will print: "I'm a global variable"


my_function()
print(global_var)  # This will print: "I'm a global variable"


global_var = "I'm a global variable"


def my_function():
    global_var = "I'm a local variable"
    print(global_var)  # Outputs: "I'm a local variable"


my_function()
print(global_var)  # Outputs: "I'm a global variable".
# То есть глобально переменная не изменилась за пределами ф-ции.

'''
Глобальными переменами обычно делают константы
'''

COMFORTABLE_TEMPERATURE = 25  # CPSLOCK - константа


def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
    return COMFORTABLE_TEMPERATURE - temperature

print(get_diff_from_comfortable_temperature(temperature=20))  # Outputs: 5

'''
Пример абсолютного зла: когда константу (глобальную переменную) в коде меняют
'''

global_var = "I'm a global variable"


def my_function():
    global global_var  # Ф-ция global объявляет, что global_var - глобальная переменная.
    global_var = "I've defined inside the scope of my_function"


print(global_var)  # Outputs: "I'm a global variable"
# Глобальная переменная не изменилась, так как мы еще не запустили ф-цию my_function()
my_function()  # А вот теперь запустили.
print(global_var)  # Outputs: "I've defined inside the scope of my_function"

'''
Пример хороший для закрепления
'''

DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False  # задали переменную внутри ф-ции с дефотным значением,
    # которое может поменяться в будущем.
    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up


print(is_leveled_up(current_experience=150, gained_experience=60))  # Outputs: True
print(is_leveled_up(current_experience=10, gained_experience=60))  # Outputs: False
