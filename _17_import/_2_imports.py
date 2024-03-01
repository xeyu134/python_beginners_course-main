from _17_import.math_operations import add, subtract
# Из папки '_17_import', модуля 'math_operations' импортируем ф-ции add и subtract.
print(add(1, 2))
print(subtract(2, 1))

from _17_import import math_operations
# Импортируем модуль целиком.
print(math_operations.add(1, 2))  # но чтобы использовать ф-цию из модуля, надо использовать ее в паре с названием модуля через точку.


from _17_import.math_operations import *  # don't do this
# Импортирует все ф-ции модуля целиком. Можно применять без названия модуля.
# Так делать не стоит, так как может возникнуть ситуация, когда название ф-ции совпадает с какой нибудь переменной.
# Если и использовать такой способ, то только до написания кода.
print(add(4, 5))
print(subtract(4, 5))

from _17_import.math_operations import add as addition
# Или можно присвоить другое название ф-ции из модуля.
print(addition(4, 5))

from math_operations import add, subtract  # possible, but not recommended
# Если модуль есть в той же папке, то можно не указывать название папки.
print(add(4, 5))
print(subtract(4, 5))

from .._15_function_advanced._2_return_mutiple_values import modify_dict  # possible, but not recommended

