# print('hello python')

# типы данны которые мы будем изучать в ближайшее время:
# int, float, boolean, str, list, None

# value = None
# a = 34
# b = 2.4
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# value = 145456
# print(value)
# s = 'hello world'
# print(s)
# print(a, b, s)
# print('{}-{}-{}'.format(s,a,b))
# print('{0}-{2}-{1}'.format(s,a,b))
# print(f'{a}-{s}-{b}')

# f = True
# print(f)

# list = [4, 5, 3, 'hello world']
# print(list)

# print('введите a')
# a = int(input())
# print('введите b')
# b = int(input())
# print(a, b)
# print(a, '+', b, '=', a+b)
# print(f'{a},{b}')

# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций **, un+, un-, *, /, //, %, +, -
# (), Сокращенные операции

# a = 2.2
# b = 2.4
# c = round((a * b), 5)
# print(c)

# a = 3
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and or, не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 != 4 and 4 != 1
# print(a)

# a = 1 < 3 > -1
# print(a)

# a = 3 > 1 or 5 < 7
# print(a)

# a = [1, 2, 3, 4]
# print(not 3 in a)

# f = [1, 2, 3, 4]
# is_odd = f[0] % 2 != 0
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a < b:
#    print(a)
# else:
#    print(b)

# username = input('Введите имя = ')
# if username == 'Foxy':
#     print('Ага, попалась ;)')
# elif username == 'Nick':
#     print('Не, ну это ни в какие ворота %)')
# elif username == 'blablabla':
#     print('Ну и имя &)') 

# Управляющая конструкция
# while

# original = 34
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй, нет!')
# print(inverted)

# Управляющая конструкция
# for

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i**3)

# r = range(5)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(5, 20, 3):
#     print(i)

# for i in 'Lisichka':
#     print(i)

# text = 'Учимся Python(у)'
# print(text[0])
# print(text[len(text)-5])
# print(text[5:len(text)-3])
# print(text[:])

# Описание функции
# def f(x):
#     if x == 1:
#         return 'целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2.3
# print(f(arg))
# print(type(f(arg)))