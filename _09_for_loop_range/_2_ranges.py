range_object = range(10)  # генерирует последовательность чисел от 0 до 9
# в перменную вводится конечное значение, которое не войдет в список
print(range_object)  # Outputs: range(0, 10)
numbers = list(range_object)  # преобразуем в список
print(numbers)  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


my_range = range(1, 10)  # задаем начало и конец
print(list(my_range))  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]


my_range = range(1, 10, 2)  # задаем еще шаг
print(list(my_range))  # Outputs: [1, 3, 5, 7, 9]


my_range = range(10, 1, -1)  # задаем обратный шаг и не включаем 1
print(list(my_range))  # Outputs: [10, 9, 8, 7, 6, 5, 4, 3, 2]


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    number = number + 1
print(numbers)  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] It doesn't work!
# int-переменная не может меняться

# чтобы изменить каждый элемент, надо найти его по индексу
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers)):  # генерируем список индексов, его кол-во == длине списка
    numbers[i] += 1  # Для каждого элемента с индексом i, добавляем 1
print(numbers)

# Кстати, "i" - стандартное обозначение переменной индекса

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers) - 1, -1, -1):  # индекс от 9 (10-1) до 0 (т.к. -1 не включаем) идем в обратном порядке (-1)
    print(numbers[i])  # переменная с индексом 9 - это 8
    numbers[i] += 1  # к 8 добавляем 1
print(numbers)  # вывод списка с обновленными элементами в индексах от 0 до 9


greeting = 'Hello, World!'
indexes = []  # список, где хранятся индексы
letter = 'o'
count = 0  # счетчик букв 'o'
for i in range(len(greeting)):
    if greeting[i] == letter:  # если элемент с индексом i равен букве 'o'
        indexes.append(i)  # добавить в список индекс i
        count += 1
print(count)  # Outputs: 2
print(indexes)  # Outputs: [4, 8]
