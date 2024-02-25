numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])  # Outputs: [0, 1, 2, 3, 4], то есть начало возвращает, но не конец
# чтобы вернуть элементы до 5-ти, конечным индексом надо указать 6
# вообще, если первый индекс - 0, то конечный индекс == кол-ву элементов на выходе
new_numbers = numbers[0:5]
print(new_numbers)  # Outputs: [0, 1, 2, 3, 4]
print(numbers[0:10])  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:len(numbers)])  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:])  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:5])  # Outputs: [0, 1, 2, 3, 4]
print(numbers[5:])  # Outputs: [5, 6, 7, 8, 9]
print(numbers[0:10:2])  # Outputs: [0, 2, 4, 6, 8], 3-ий парамет - забираем каждый второй элемент
print(numbers[::2])  # Outputs: [0, 2, 4, 6, 8]
print(numbers[3:2])  # Outputs: [], так как это не логично, но Python не ругается
print(numbers[0:20])  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-5:-1])  # Outputs: [5, 6, 7, 8] - последние 4 элемента
print(numbers[::-1])  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - "-1" - через один, но в обратном порядке


string = "Hello, world!" # со строками можно делать то же самое, что и списком
print(string[0:5])  # Outputs: 'Hello'
print(string[7:])  # Outputs: 'world!'
print(string[::2])  # Outputs: 'Hlo ol!'
print(string[::-1])  # Outputs: '!dlrow ,olleH'
print(string[2:1])  # Outputs: ''fd

"""3 способа развернуть список"""
print(numbers[::-1])
print(numbers.reverse())
print(list(reversed(numbers))) # ф-ция reversed возвращает тип list_reverseiterator
# поэтому надо конвертнуть его обратно в list