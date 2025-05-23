# Задача 13.
# При заданном целом числе n посчитайте n + nn + nnn.

# Приглашение к вводу команды. В нашем случае, можно вводить только целочисленные (int).
n = int(input('Введите целое число n:~$ '))

# Преобразуем n в строку (str) и повторяем 2 раза (*2), а затем преобразуем обратно в число (int).
# В Python умножение строк на целое число приводит к их повторению.
nn = int(str(n) * 2)
nnn = int(str(n) * 3) # Здесь всё тоже самое, только повторяем 3 раза, а не 2.

# Считаем сумму.
# То есть, если ввести 2, то nn = 22, nnn = 222.
# Сумма будет 2 + 22 + 222 = 246.
result = n + nn + nnn

# Принтуем результат в терминал.
print('Задача 13, решение:')
print('Результат:', result)