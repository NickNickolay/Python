# Вывести квадрат числа

# number = int(input('Введите число = '))
# print(f'Квадрат числа {number} равен {number**2}')

# По двум заданным числам проверять является ли первое квадратом второго

# num1 = int(input('Задайте первое число = '))
# num2 = int(input('Задайте второе число = '))
# if num1 == num2 ** 2:
#     print(f'{num1} Является квадратом {num2}')
# else:
#     print(f'Число {num1} не является квадратом {num2}')


# Даны два числа. Показать большее и меньшее число

# Fnumber = int(input('Введите первое число = '))
# Snumber = int(input('Ведите второе число = '))
# if Fnumber < Snumber: 
#     print(f'Минимальное число = {Fnumber} Максимальное члисло = {Snumber}')
# else :
#     print(f'Минимальное число = {Snumber} Максимальное члисло1 {Fnumber}')


# По заданному номеру дня недели вывести его название

# dayNumber = int(input('Введите число = '))
# if dayNumber == 1:
#     print(f'Понедельник')
# elif dayNumber == 2:
#     print(f'Вторник')
# elif dayNumber == 3:
#     print(f'Среда') 
# elif dayNumber == 4:
#     print(f'Четверг')
# elif dayNumber == 5:
#     print(f'Пяятница')
# elif dayNumber == 6:
#     print(f'Суббота')
# elif dayNumber == 7:
#     print(f'Воскресенье')
# else:
#     print(f'Нет такого дня')

# Найти максимальное из трех чисел


# a = int(input('Введите первое число = '))
# b = int(input('Введите второе число = '))
# c = int(input('Введите третье число = '))
# if a > b > c:
#     max = a
# elif b > a > c:
#     max = b
# else: 
#     max = c
# print(f'Максимальное число {max}')



# Написать программу вычисления значения функции y = f(a)

# def f(a):
#     y = a**2 + 2*a
#     return y 

# x = int(input('Введите число = '))
# print(f(x))

# Выяснить является ли число чётным

# number = int(input('Введите число = '))
# if number % 2 == 0:
#     print(f'{number} Четное')
# else:
#     print(f'{number} Не четное')

# Показать числа от -N до N

# a = int(input('Введите число = '))
# for i in range(-a, a+1):
#     print(i)

# Показать четные числа от 1 до N

# a = int(input('Введите число = '))
# for i in range(1, a+1):
#     if i % 2 == 0:
#          print(i)


# Показать последнюю цифру трёхзначного числа

# a = int(input('Введите трехзначное число = '))
# b = a // 100
# print(b)

# Показать вторую цифру трёхзначного числа

# a = int(input('Введите трехзначное число = '))
# b = a // 10 
# c = b % 10
# print(c)


# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

# num = int(input('Введите число от 10 до 99 = '))
# num1 = num//10
# num2 = num % 10
# if num1 > num2:
#     print(f'{num1} Наибольшее число')
# else:
#     print(f'{num2} Наибольшее число')

# Удалить вторую цифру трёхзначного числа

# number = int(input('Введите трехзначное число = '))
# number1 = number // 100
# number2 = number % 10
# print(f'{number1}{number2}') 

# Выяснить, кратно ли число заданному, если нет, вывести остаток.

# a = int(input('Задайте число = '))
# b = int(input('Проверка на кратность:Введите число = '))
# if a % b == 0:
#     print(f'Число {a} кратно {b}')
# else:
#     print(f'Не кратно! Остаток {a%b}')

# Найти третью цифру числа или сообщить, что её нет

# a = int(input('Введите число = '))
# if a < 0:
#     a = a * -1
# if a < 100:
#     print('Третьей нет, увы:(')
# else:
#     b = str(a)
#     print(f'Третья цифра {b[2]}')
