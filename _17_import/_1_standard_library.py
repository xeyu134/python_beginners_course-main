my_int = 1

print(globals().keys())  # отображает все перменные, ф-ции классы в коде. А также модули

import random

my_list = [1, 2, 3]
print(random.choice(my_list))  # этот метод выбирает рандомное значение из списка.
print(globals().keys())

print(dir(random))  # от directory - все все ф-ции random 

import builtins

print(dir(builtins))  # find print, range, dict, list, etc.


