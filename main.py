# # Кортежи.
#
# tuple1 = tuple()
# list1 = ['a', 'b', 'c']
# tuple2 = tuple(list1)
# #
# # tuple3 = tuple(('aa', 'bb', 'cc', 'dd'))
# # tuple4 = tuple((list1 + list2))
# #
# # print(tuple3[2])
# # for i in tuple3:
# #     print(i)
#
# # cmp(tuple1, tuple2) # сравнение двух tuple
# # len(tuple1)
# # all(tuple1) - возвращает true, если все элементы кортежа оцениваются как true, если кортеж пуст, возвращает true.
# # any(tuple1) - проверка хотябы одного значения как true, иначе возвращает false, аналогично пустому кортежу.
# # max, min, sum, sorted
#
# # set множества, создание.
# our_set = set()
# our_set2 = {0}
# print(our_set, type(our_set))
# # Добавление нового элемента.
# our_set.add('tomato')
# our_set2.add('potato')
# # Проверка элемента в множестве.
# x = 'tomato'
# print(x in our_set)
# print(x in our_set2)
# # Функции множеств, проверка.
# print(our_set.isdisjoint(our_set2)) # Возвращает значение True, если в множестве нет общих элементов.
# our_set3 = our_set.union(our_set2) # Объединяет множества.
# our_set.update(our_set2) # Расширение множества.
# print(our_set)
# print(our_set3)
# # issubset - проверка на содержание в себе другого множества.
#
# print(our_set2.issubset(our_set3)) # Проверка 2 на содержание в 3.
# print(our_set2.issuperset(our_set3)) # Проверка 3 на содержание в 2.

# our_products = {'Apple', 'Tesla', 'McDonalds'}
# range_of_the_company1 = {'Samsung', 'Sony'}
# range_of_the_company2 = {'Apple', 'IBM', 'Tesla'}
# range_of_the_company3 = {'BMW', 'Tesla', 'Ferrari'}
#
# # Предоставляет множество общих элементов (пересечение множеств).
# print(our_products.intersection(range_of_the_company1))
# print(our_products.intersection(range_of_the_company2))
# print(our_products.intersection(range_of_the_company3))
#
# # difference - разница множеств.
# print(our_products.difference(range_of_the_company1))
# print(our_products.difference(range_of_the_company2))
# print(our_products.difference(range_of_the_company3))
#
# # symmetric_difference() - симметрическая разница двух множеств.
# print(our_products.symmetric_difference(range_of_the_company1))
# print(our_products.symmetric_difference(range_of_the_company2))
# print(our_products.symmetric_difference(range_of_the_company3))
#
# # intersection_update() - метод изменяет само множество.
# # differcence_update() - метод изменяет само множество.
# # symmetric_difference_update() - метод изменяет само множество.
#
# # discard() - может удалять не существующие элементы.
# # remove() - не может удалять не существующие элементы.
#
# our_products.discard('Apple')
# our_products.discard('Mercedes')
# print(our_products)
#
# our_products.remove('McDonalds')
# our_products.remove('Mercedes') # пример ошибки.
# print(our_products)
#
# our_products.pop() # удаление случайного элемента.
#
# # frozenset - неизменяемый тип множеств.
# my_frozenset = frozenset()

# Задание 1.
tuple = (('Apple', 'Apple', 'Strawberry', 'Banana'))
value1 = input('Введите название фрукта:~$ ')
print(tuple.count(value1))

# Задание 2.
tuple = (('Apple', 'Apple', 'Strawberry', 'banana', 'bananamango', 'Mango', 'Strawberry-banana'))
value1 = input('Введите слово для поиска:~$ ')
count = ' '.join(tuple).count(value1)
print(count)

# Задание 3.
tuple = (('Mercedes', 'Mercedes', 'Mercedes', 'BMW', 'Toyota', 'Subaru'))
value1 = input('Введите название автомобиля:~$ ')
value2 = input('Введите слово для замены:~$ ')