# Задача 1. Выведите все элементы, которые меньше 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# В данном случае мы используем списковое включение.
# Проходимся циклом по списку и говорим ему, чтобы вывел все значения "а", которые меньше 5.
result = [x for x in a if x < 5]
print('Задача №1, решение:', result)