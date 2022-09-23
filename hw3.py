# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

#
# def my_div():
#
#     try:
#         x = int(input('Enter x:'))
#         y = int(input('Enter y:'))
#         res = x / y
#     except ZeroDivisionError:
#         return('cant divide by zero')
#     return res
#
#
# s = my_div()
# print(s)

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
# аргументы. Осуществить вывод данных о пользователе одной строкой.
#
# def pers_dat(first_name, last_name, age, city, email, tel):
#     print(f'pers_dat.first_name: {first_name} last_name: {last_name} age: {age} city: {city} email: {email} tel:{tel}')
#
#
# pers_dat(first_name='Ivan',  last_name='Ivanov', age=1990, city='Rostov', email='ivanov@mail.ru', tel=+984756395)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.
#
#
# def my_func():
#
#     try:
#         a = int(input('Enter a:'))
#         b = int(input('Enter b:'))
#         c = int(input('Enter c:'))
#
#         d = a + b
#         e = a + c
#         g = b + c
#
#         if d > e and d > g:
#             return d
#         elif e > d and e > g:
#             return e
#         else:
#             return g
#     except ValueError:
#         print('No number')
#
#
# (my_func())

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Sposob1

# def my_func(x, y):
#
#     y = int(y)
#     if x > 0 > y:
#         res = x ** y
#         return res
#     else:
#         print('nevernyj vvod dannych')
#
#
# print(my_func(4, -1))

# Sposob2
#
# def my_func(x, y):
#
#     y = int(y)
#     if y < 0 < x:
#         y = abs(y)
#         i = 1
#         while i <= y:
#             b = (1 / x) * 1
#             i = i + 1
#             return f'result = {b * (1 / x)}'
#     else:
#         print('nevernyj vvod dannych')
#
#
# s = my_func(3, -4)
# print(s)

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом
# и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

# def num_sum():
#     res = 0
#     while True:
#         li = input('Enter data:').split()
#         for num in li:
#             num = int(num)
#             if num == 'stop':
#                 return res
#             else:
#                 res += int(num)
#                 return
#         print('num_sum=', res)
#
#
# print(num_sum())


# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# def int_func():
#     slovo = input('Input word:').lower().title()
#     print(slovo)
#
#
# int_func()
