# Задача 18.
# Посчитайте, сколько раз символ встречается в строке.

# Ввод строки и символа для поиска.
print('Задача 18, решение:')
string = input("Введите строку:~$ ")
char = input("Введите символ для поиска:~$ ")

# Подсчет количества вхождений символа в строке.
# Считаем с помощью метода count.
count = string.count(char)

# Вывод результата. Используем f-строку. Передаём в неё переменные char и count (количество посчитанных символов).
print(f"Символ '{char}' встречается в строке {count} раз(а).")