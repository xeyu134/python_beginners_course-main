file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
for file_name in file_names:  # для элемента из списка (у каждого есть название переменной)
    print(file_name)
# сколько элементов в списке, столько и интераций цикла
# и столько же раз будет обновляться переменная file_name

greeting = 'Hello, World!'
for char in greeting:
    print(char)  # получится эта же фраза, но в столбик


greeting = 'Hello, World!'
count_o = 0  # переменная-счетчик буквы 'o', по умолчанию 0
for char in greeting:
    if char == 'o':
        # count_o = count_o + 1
        count_o += 1  # "+" - прибавить, "=" - к существующей. Можно еще "-" и "*".
print(count_o)  # переменная обновилась до 2, так как было 2 цикла по условию


students = ["Alice", "Bob", "Charlie", "David"]
for student in students:
    print(student)
    for char in student:
        print(char)  # в итоге выдается имя студента, а потом его буквы по отдельности


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    # Skip odd numbers
    if num % 2 != 0:
        continue  # пропускаем цикл, т.е. нечетные числа
    print(num)  # в остальных циклах принтуем, и запускаем следующий цикл


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    # Break the loop if the number is 10
    if num == 10:
        break  # прервать следующие, и не запускать следующие
    print(num)  # вывод будет до 9
