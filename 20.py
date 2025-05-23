# Задача 20.
# С помощью анонимной функции извлеките из списка числа, делимые на 15.

# Исходный список чисел.
numbers = [10, 15, 20, 30, 45, 50, 60, 75, 90, 100]

# Используем filter и лямбда-функцию для извлечения чисел, делимых на 15.

# filter(...) - это встроенная функция Python, которая принимает два аргумента: функцию и итерируемый
# объект, например, список. Она применяет указанную функцию к каждому элементу итерируемого списка объекта
# и возвращает только те элементы, для которых функция вернула значение True.

# lambda x: x % 15 == 0: это лямбда-функция, которая принимает один аргумент x (каждое число из списка numbers)
# и возвращает True, если x делится на 15 без остатка (т.е. x % 15 равно 0). Если x не делится на 15,
# функция вернёт False.

# numbers - это список чисел, к которому будет применяться фильтрация.

# list(...) - функция list преобразует результат, возвращаемый функцией filter, в список.
# Поскольку filter возвращает специальный объект (итерируемый), а не список, использование list
# позволяет получить обычный список, который можно использовать в дальнейшем.

divisible_by_15 = list(filter(lambda x: x % 15 == 0, numbers))

# Вывод результата.
print('Задача 20, решение:')
print(divisible_by_15)