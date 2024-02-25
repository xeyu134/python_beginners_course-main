'''
Цикл for имеет определенное кол-во интераций.
Как правило, сколько элементов в колекции, столько и циклов.
А цикл while не ограничен этим и завершается по условию.
Чаще всего используется для подсчета элементов по какому-то условию.
'''

'''
Пример стандартный
'''
counter = 1
while counter <= 5:
    print(f'Counter is: {counter}')  # Outputs: 1, 2, 3, 4, 5
    counter += 1

'''
Пример с удалением элементов из списка
'''
my_list = [0, 1, 2]
while my_list:
    element = my_list.pop()  # Присваивает переменной последний элемент списка
    # и удаляет его из списка
    print(f"element: {element}")  # Outputs: 2, 1, 0
print(my_list)  # Outputs: [], то есть цикл удалил все элементы из исконного списка.

'''
Пример бесконечного цикла
'''
# while True:
#     print("Infinite loop!")

'''
Пример бесконечного цикла, где программу останавливает пользователь
'''
while True:
    answer = input("Enter a number: ")
    if answer == 'quit':
        break  # прерывает цикл, и "Enter a number: " больше не всплывет.
    print(f"You entered: {answer}")

for number in range(10):
    print(number)
    if number == 2:
        break
