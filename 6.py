# Задача 6.
# Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.

# Заводим функцию, которая принимает в себя два параметра - num и base.
# num - это целое число, которое нужно преобразовать.
# base - это основание системы исчисления, в которую нужно преобразовать число.
def int_to_string(num, base):

    # Если num отрицательное, функция рекурсивно вызывает саму себя с положительным значением, то есть num
    # и добавляет перед результатом символ "-", чтобы указать, что число отрицательное.
    if num < 0:
        return '-' + int_to_string(-num, base)

    # Если num равно нулю, функция возвращает строку "0", так как в любой системе исчисления ноль
    # представлен как ноль.
    elif num == 0:
        return '0'

    # Если num положительное и не равно нулю, создаётся пустой список digits, который будет
    # использоваться для хранения цифр результата в обратном порядке.
    else:
        digits = []

        # Цикл while будет выполняться до тех пор, пока num не станет равным нулю.
        # Он используется для извлечения цифр числа в заданной системе исчисления.
        while num:

            # remainder хранит остаток от деления num на base. Это значение соответствует
            # последней цифре числа в указанной системе исчисления.
            remainder = num % base

            # Если остаток меньше 10, он просто преобразуется в строку и добавляется в список digits.
            # Это соответствует цифрам от 0 до 9.
            if remainder < 10:
                digits.append(str(remainder))

            # Если остаток 10 или больше, он преобразуется в символ от 'А' до 'Z'. Это делается путём
            # вычитания 10 из остатка и добавления к коду символа 'А' (код символа 'А' равен ord('A'),
            # что равно 65). Таким образом, остатки 10, 11, 12 и т.д. будут преобразованы в 'A', 'B', 'C'
            # и так далее, соответственно...
            else:
                digits.append(chr(remainder - 10 + ord('A')))

            # num делится на base с использованием целочисленного деления ( // ), что позволяет уменьшить
            # num для следующей итерации цикла и извлечения следующей цифры.
            num //= base

        # После завершения цикла, список digits содержит цифры числа в обратном порядке (от младших к старшим).
        # digits[::-1] переворачивает список, а ''.join(...) объединяет все элементы списка в одну строку,
        # которая и будет результатом.
        return ''.join(digits[::-1])

# Примеры использования.
print('Задача 6, решение №1:')
print(int_to_string(255, 16)) # Здесь мы преобразуем число 255 в шестнадцатеричную систему исчисления.
print(int_to_string(10, 2)) # Здесь 10 в двоичную систему исчисления.
print(int_to_string(-42, 10)) # Здесь -42 в десятичную.

# Готовое решение с сайта TProger.ru
print('Задача 6, решение №2:')
print(int('ABC', 16))