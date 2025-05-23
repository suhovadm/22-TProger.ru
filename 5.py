# Задача 5. Найдите три ключа с самыми высокими значениями
# в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

# Создаём сам словарь. Здесь самые высокие - это b, e и c.
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# Сортируем словарь по значению в порядке убывания (reverse=True)
# и извлекаем первые три ключа [:3] - это и будут наши b, e и с.
top_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

# Выводим результат переменной выше в терминал.
# Мы должны получить b, e и c, так как они имеют наивысшее значение.
print('Задача №5, решение:', top_keys)