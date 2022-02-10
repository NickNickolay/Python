#31. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.


# def Natur1(n):
#     list = [1]
#     pocket = 1
#     for i in range(1, n+1):
#         pocket *= -3
#         list.append(pocket)
#     return list
# print(Natur1(5))

#32.  Для натурального N создать словарь индекс-значение,
#  состоящий из элементов последовательности 3k + 1.

# def Sequence(k):
#     return 3*k+1

# def Natur(N):
#     for i in range(1, N+1):
#         return i


# dictionary = \
#     {
#        f'{1}': f'{Sequence(1)}',
#        f'{2}': f'{Sequence(2)}'
#     }

# print(dictionary)


#33. Пользователь задаёт две строки. 
# Определить количество количество вхождений одной строки в другой.

# def numberOfOccurrences(string1, string2): 
#     text = ' ' 
#     count = 0 
#     u = 0 
#     while u < len(string2): 
#         for i in string1: 
#             for j in string2: 
#                 if i == j: 
#                     count += 1 
#                     # text += i 
#         u +=1 
#     return (count // u) // u 
    
# s1 = input("Введите строку>>> ") 
# s2 = input("Введите искомую часть>>> ") 
# print(f'Количество вхождений {s2} в {s1} составляет {numberOfOccurrences(s1, s2)} раз(а)')



#34. Подсчитать сумму цифр в вещественном числе.

# def SumNum(num):
#     num1 = str(num)
#     res = 0
#     for i in num1:
#         if i !='-' and i !='.':

#             res += int(i)
#     return res


# a = input('Введите число = ')    
# print(SumNum(a))
# print(f'Число {a} в сумме = {SumNum(a)}')


#35. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]


# def Product(N):
#     list = [1]
#     cell = 1
#     x = 2
#     for i in range(1, N):
#         cell *= x
#         list.append(cell)
#         x += 1
#     return list
# print(Product(3))
    


#36. Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

# def List(n): 
#     list = [] 
#     sum = 0 
#     for i in range(1, n+1):  
#         action = (1 + 1 / i)**i 
#         list.append(action) 
#         sum += action
#         i+=1 
#     print(list) 
#     return sum 
 
# print(List(2))


#37. Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число

# from random import randint
# def list(N):
#     lst = []
#     count = 0
#     for i in range(0, N):
#         count = randint(-N, N)
#         lst.append(count)
#     return lst
# list1 = list(5)
# print(list1)

# def ProductElements(list):
#     result = 1
#     path = 'ProductElements.txt'
#     data = open(path, 'r')
#     for i in range(0, len(list)):
#         for line in data:
#             i = int(line)
#             temp = list[i]
#             print(f'{i}, {temp}')
#             result *= temp
#     return result
#     data.close()
# print(ProductElements(list1))



#38. Реализовать алгоритм перемешивания списка. 

# from random import randint
# lst = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
# count = len(lst)  // 2
# while count >= 0:
#     count1 = randint(0, len(lst)-1)
#     temp = lst[count1]
#     lst.pop(count1)
#     lst.append(temp)
#     count -= 1
# print(lst)


#39. Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

# def randomNumber(N):
#     list = []
#     list2 = []
#     for i in range(-N, N+1):
#         list.append(i)
#     for j in list:
#         k = (j**2 - 4*j - 3*j)
#         list2.append(j+k)
#     return list2
       
# print(randomNumber(5))


#40. Определить, присутствует ли в заданном списке строк, некоторое число 

# lst = ['5y8', 't1f', 'gfh', '390']
# SomeNum = '7'

# def SearchNumber(list, SearchNumber):
#     count = 0
#     for i in list:
#         str = i
#         for j in str:
#             if j == SearchNumber:
#                 count += 1
#     if count > 0:
#         print(f'Некоторое число {SomeNum} присутствует')
#     else:
#         print(f'Некоторое число {SomeNum} отсутствует')

# SearchNumber(lst, SomeNum)


#41. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

# lst = ['5t1y8', 't153f', 'gfh', '390', '5t8yfh']
# SomeNum = 'gf'

# def SearchPos(list, SomeNum):
    
#     temp = 0
#     for i in range(0, len(list)):
#         str = list[i]
#         count = 0
#         for j in str:
#             for k in SomeNum:
#                 if k == j:
#                     count += 1
#                     if count == len(SomeNum):
#                         temp += 1
#                         if temp == 2:
#                             return i

# position = SearchPos(lst, SomeNum)
# if position == None:
#     print(f'Его нет')
# else:
#     print(f'{SomeNum} вошло второй раз на позицию {position}')



#42. Найти сумму чисел списка стоящих на нечетной позиции

 
# def sumOddPositionOfList(list): 
#     result = 0 
#     for i in range (len(list)): 
#         if i % 2 == 0: 
#             result += int(list[i]) 
#             i += 1 
#     return result
 
# lst = [1, 2, 3] 
# print(sumOddPositionOfList(lst))

#43. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# def ProductListPairs(list):
#     res = []
#     N = len(list) - 1
#     K =  len(list) 
#     if K % 2 != 0:
#         K = K // 2 + 1
#     else:
#         K = K // 2
#     for i in range(0, K):
#         K1 = list[i] * list[N]
#         N -= 1
#         i += 1
#         res.append(K1)
#     return res

# list1 = [1, 2, 3, 4, 5]
# Get = ProductListPairs(list1)
# print(Get)


#44. В заданном списке вещественных чисел найдите разницу между максимальным
#  и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import math

# def RealNumberlist(list):
#     fract = []
#     for i in list:
#         c = math.floor(i)
#         f = round((i - c), 3)
#         fract.append(f)
#     return fract

# list1 = [1.3, 1.6, 3.1, 5, 10.01]
# list2 = RealNumberlist(list1)

# def DifMaxMin(list):
#     min = list[0]
#     max = list[0]
#     for i in list:
#         if(i != 0 and i < min):
#             min = i
#         if(i != 0 and i > max):
#             max = i
#     return (max, min)
# print(DifMaxMin(list2))



#45. Написать программу преобразования десятичного числа в двоичное

# def Conversion(num):
#     temp = 0
#     list1 = []
#     while num > 0:
#         temp = num % 2
#         list1.append(temp)
#         num = num // 2
#     list2 = []
#     N = len(list1) - 1
#     while N >= 0:
#         B = list1[N]
#         list2.append(B)
#         N -= 1
#     return list2

# Total = Conversion(34)
# print(Total)

#46. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов


# def Fibonachi(N):
#     if N < 2: return 1 
#     return Fibonachi(N-1) + Fibonachi(N-2)

# def Fibonachi1(n):
#     list1 = []
#     list2 = []
#     Fib = 1
#     Fib1 = 0
#     for i in range(n):
#         Fib, Fib1 = Fib1, Fib+Fib1
#         list1.append(Fib)
#     print(list1)
#     Fib = 1
#     Fib1 = 0
#     for i in range(n):
#         Fib, Fib1 = Fib1, Fib+Fib1
#         list2.append((-1)**(i+1)* Fib1)
#     print(list2)

# Fibonachi1(10)


#47.????????????????? Строка содержит набор чисел. Показать большее и меньшее число

# def KitMaxMin(str):
    
#     min = 0
#     max = 0
#     for i in str:
#         num = int(i)
#         if num >= max:
#             max = num
#         if max <= min:
#             min = num
#     return (max, min)

# str1 = input('Введите набор чисел = ') 
# print(KitMaxMin(str1))


#48 Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*

# def quadEquation(a, b, c): 
#     if a != 0 and b!= 0 and c!= 0: 
#         D = b**2 - 4 * a * c 
#         print(D) 
#         if D < 0: print('Уравнение не имеет корней') 
#         elif D == 0: 
#             x = -b/(2*a) 
#             print(f'x = {x}') 
#         else: 
#             x1 = (-b + D**0.5)/(2*a) 
#             x2 = (-b - D**0.5)/(2*a) 
#             print(f'x1 = {x1}, x2 = {x2}') 
#     elif a != 0 and b == 0 and c == 0: 
#         print('x = 0') 
#     elif a != 0 and b == 0 and c != 0: 
#         temp = - c / a 
#         if temp < 0: 
#             print('Уравнение не имеет корней') 
#         elif temp > 0: 
#             x1 = (-c / a)**0.5 
#             x2 = -(-c / a)**0.5 
#             print(f'x1 = {x1}, x2 = {x2}')    
#     elif a == 0 and b != 0: 
#         x = -c / b 
#         print(f'x = {x}') 
     
 
        
# num1 = 0 
# num2 = 2 
# num3 = -3 
 
# quadEquation(num1, num2, num3)

# import math

# print("Введите коэффициенты для уровнения")
# print("ax^2 + bx + c = 0:")
# a =  float(input("a = "))
# b =  float(input("b = "))
# c =  float(input("c = "))

# discr = b**2 - 4 * a * c
# print("Дискримант D = %.2f" % discr)

# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2*a)
#     x2 = (-b - math.sqrt(discr)) / (2*a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2*a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")

#49. Найти НОК двух чисел ???????????

# a = 12
# b = 49

# nok = list((a, b, x) for x in range(1, lambda a, b, x: (a*b) + 1) if (x % a == 0) and (x % b == 0))
# print(nok)

#50. Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001, π = 3.141. 10-1≤d≤10-10





#51. Составить список простых множителей натурального числа N


#52. Дана последовательность чисел. 
# Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]



#53. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = 5
# equation_str = reduce(lambda x,y:  x+y, [str(i) + '**x' + str(random.randint(0, 100)) + ' + ' for i in range(k + 1)])
# print(equation_str)
# equation_str = equation_str[-4: -len(equation_str) - 1: -1]
# equation_str += ' = 0'
# print(equation_str)
# with open('ex53.txt', 'w') as file:
#     file.write(equation_str)


#54. Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.



# 55. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.



# 56. Дан список чисел. Выделить среди них числа, удовлетворяющие 
# условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.



# 57. Дан список чисел. Выделить среди них максимальное количество чисел,
#  удовлетворяющих условию предыдущей задачи. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# 58. Напишите программу, удаляющую из текста все слова содержащие "абв".



# 59. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом" 
#60. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
#61. Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;



#62. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных файлах





#63. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
