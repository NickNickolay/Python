#17. По двум заданным числам проверять является ли одно квадратом другого.

# a = int(input('Вветите первое число = '))
# b = int(input('Введите второе число = '))
# if a == b**2:
#     print(f'Число {a} является квадратом {b}')
# elif b == a**2:
#     print(f'Число {b} является квадратом {a}')
# else:
#     print(f'Нет')

#18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# x = 0
# y = 1
# f1 = not(0 or 1)
# f2 = not 0 and not 1
# print(f1 == f2)


#19. Определить номер четверти плоскости, в которой находится точка 
# с координатами Х и У, причем X ≠ 0 и Y ≠ 0

# a = int(input('Введите координату X = '))
# b = int(input('Введите координату Y = '))
# if a > 0 and b > 0:
#     print('Первая четверть')
# elif a < 0 and b > 0:
#     print('Вторая четверть')
# elif a < 0 and b < 0:
#     print('Третья четверть')
# else:
#     print('Четвертая четверть')





#20. Задать номер четверти, показать диапазоны для возможных координат

# def TrueOrNot(x, y):
#     for x in range(2):
#         for y in range(2):
#             f1 = not(x or y)
#             f2 = not x and not y
#             res = f1==f2
#             print(res)
# TrueOrNot(1,0)

#21. Программа проверяет пятизначное число на палиндромом.

# a = input('Введите пятизначное число = ')
# if a[0] == a[4] and a[1] == a[3]:
#     print('Палиндром')
# else:
#     print('Не палиндром')


#22. Найти расстояние между точками в пространстве 2D/3D

# def FindDistance3D(x1,y1,z1,x2,y2,z2):
#     line = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
#     return line
# print(FindDistance3D(2, 2, 2, -1, -1, -1))

# def FindDistance2D(x1,y1,x2,y2):
#     line = ((x1-x2)**2+(y1-y2)**2)
#     return line
# print(FindDistance2D(2, 2, 2, -1))


#23. Показать таблицу квадратов чисел от 1 до N

# N = int(input('Введите число N = '))
# for i in range(1,N+1):
#     res = i**2
#     print(f'{i} ^ 2 = {res} ')
#     i += 1



#24. Найти кубы чисел от 1 до N

# x = int(input('Введите число = '))
# def CubeNumber(x):
#     for i in range(1, x+1):
#         print(i**3, end='  ')
# CubeNumber(x)

#25. Найти сумму чисел от 1 до А

# def SumNum(a):
#     res = 0
#     for i in range(1, a+1):      
#         res += i               
#         i += 1              
#     return res

# A = int(input('Введите число a = '))
# print(SumNum(A))    


#26. Возведите число А в натуральную степень B используя цикл

# a = int(input('Введите число = '))
# b = int(input('Введите степень = '))
# def Degree(a,b):
#     for i in range(0,b+1):
#         print(f'Число {a} в степени {i} = {a**i}')
# Degree(a, b)

#27. Определить количество цифр в числе


# def CollSymbol(a):
#     col = 0
#     while a > 0:
#         a = a // 10
#         col += 1
#     return col 

# a = int(input('Введите любое число = '))    
# print(CollSymbol(a))




# 28. Подсчитать сумму цифр в числе

# def SumNum(num):
#     num1 = str(num)
#     res = 0
#     for i in num1:
#         res += int(i)
#     return res


# a = input('Введите число = ')    
# print(SumNum(a))
# print(f'Число {a} в сумме = {SumNum(a)}')
      


 

#29. Написать программу вычисления произведения чисел от 1 до N

# def ProductNum(N):
#     res = 1
#     for i in range(1, N+1):
#         res *= i 
#         i += 1
#     return res
# A = int(input('Введите число = '))
# print(ProductNum(A))

  
#30. Показать кубы чисел, заканчивающихся на четную цифру 


# def CubeNumber(x):
#     for i in range(1, x+1):
#         if i % 2 == 0:
#             res = i**3
#             print(f'{res}')

# a = int(input('Введите число = '))        
# CubeNumber(a)    



