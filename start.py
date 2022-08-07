# print('Hello word!')

# a=17/2*3+2
# print(a)

# a=2+17/2*3
# print(a)
# a = 19 % 4 + 15 / 2 * 3
# print(a)

# a = (15 + 6) - 10 * 4
# print(a)
# a = 17 / 2 % 2 *3**3
# print(a)

# a = 17 / 2 % (2 * 3 ** 3)
# print(a)

# a = 11
# b = 1.5
# c = a - 3 * b
# print(c)

# A = 2
# P = 5
# print(A, P)


# a = map(int, input("enter a:").split())
# v = a * a * a
# s = 4 * a * 2

# print("v:", v)
# print("s", s)


# a = int(input("enter a:"))
# v = a * a * a#s = 4 * a * a
# print("v:", v)
# print("s", s)

# h = int(input("enter h:"))
# print('h:',h*24,'m:',h*1440, 's:', h*86400)


# a=182
# c=7
# print (a//c)

# a, b = map(int, input("enter a b:").split())
# c = 30
# x = (a // c) * (b // c)
# print('Можно отрезать', x, 'квадратов')


# number = int(input('введите трехзначное число:'))
# z=number%10
# y=number//10%10
# x=number//100
# print(z, y, x)


#s = int(input())
#h = s // 3600
#m = h // 60
#s = h % 60
#print(h, 'часов')
#print(m, 'минут')
#print(s, 'секунд')

#N = int(input())
#x = 100
#y = 50
#z = 10
#l = 1
#a = N // 100
#b = N % 100 // 50
#c = N % 100 % 50 // 10
#d = c % 10
#print(a, 'купюры по 100 рублей')
#print(b, 'купюры по 50 рублей')
#print(c, 'купюры по 10 рублей')
#print(d, 'купюры по 1 рублей')


#h = int(input('h:'))
#x1 = int(input('x1:'))
#x2 = int(input('x2:'))
#z = h / (x1 - x2)
#print(z)



#Напишите программу, которая проверяет последнюю цифру числа. Если последняя цифра числа 3, то вывести Truo иначе False.
#n = int(input('Введите число'))
#if n % 10 == 3:
#   print('True')
#else:
#print('False')


#Напишите программу, которая выводит True, если хотя бы одно из чисел А,В,С, отрицательно. Если нет, вывести False. Числа вводятся с клавиатуры в одной строке.
#A, B, C = map(int, input("enter A B C:").split())
#if A % 2 != 0 or B % 2 != 0 or B % 2 != 0:
#print('Tru')
#else:
#print('False')


#Верно ли, что целые n и k имеют одинаковую четность?
#n = int(input())
#k = int(input())
#if n % 2 == 0 and n % 2 == 0 or n % 2 != 0 and n % 2 != 0:
#print('Tru')
#else:
#print('False')


#Найдите количество четных чисел среди заданных трех целых числ. В ответ вывести количество четных чисел.
#a, b, c = map(int, input().split())
#count = 0
#if a % 2 == 0:
#count += 1
#if b % 2 == 0:
#count += 1
#if c % 2 == 0:
#count += 1
#print(count)

#Напишите программу, которая выводит True, если X кратно 3 и заканчивается на 5. Число Х вводится с клавиатуры.
#X = int(input())
#if X % 3 == 0 and X % 10 == 5:
#print("True")
#else:
#print('False')


#Дано двузначное число. Определить, является ли сумма его цифр двухначным значением? (Yes/No)
#s = int(input())
#x = s % 10
#y = s // 10
#if 100 > (x + y) >= 10:
#print('Yes')
#else:
#print('No')

# Дано четырехзначное число. Проверить, одинаковы ли все цифры в нем.
# namber = int(input())
# if namber % 1111 == 0:
#  print('Yes')
# else:
# print('False')

#Напишите программу, принимающую на вход год и выводящую "Високосный", если в этом году действительно 366 дней,и "Не високосный" иначе.
#Год считается високосным, если его номер делится на 4, но не делится на 100 или же делится на 400.

#year = int(input())
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#print('True')
#else:
#print(' False')


#Определить, являются ли поля (x1, y1) и (x2, y2) одного цвета?

#x1, y1 = map(int, input('Введите координаты первой фигуры').split())
#x2, y2 = map(int, input('Введите координаты второй фигуры').split())
#if x1 == x2 and y1 == y2 and (x1, y1, x2, y2 <= 8):
#print('Поля одного цвета')
#else:
#print('Поля не одного цвета')

#На поле (x1,y1) расположен ферзь. Угрожает ли он полю (x2,y2)
#x1, y1 = map(int, input('Введите координаты ферзя').split())
#x2, y2 = map(int, input('Введите координаты поля').split())
#if x1 == x2 or y1 == y2 and (x1, y1, x2, y2 <= 8):
#print('Ферзь угрожает полю')


#На поле (x1,y1) стоит ладья, на поле (x2,y2) - пешка. Определить, бьет ли ладья пешку, пешка - ладью  или фигуры не угрожают друг другу.
# x1, y1 = map(int, input('Введите координаты ладьи').split())
# x2, y2 = map(int, input('Введите координаты пешки').split())
# x1, y1, x2, y2 <= 8
# if x1 == x2 or y1 == y2:
#     print('Ладья бьет пешку')
# if x1 == x2 + 1 and y2 == y1 + 1 or y2 == y1 - 1:
#     print('Пешка бьет ладью')
# else:
#     print('Фигуры не угрожают друг другу')


#На поле (x1,y1) стоит слон, на поле (x2,y2) - конь. Определить, бьет ли слон коня, конь - слона или фигуры не угрожают друг другу.


#Вывести число 10 20 раз столбиком


# for i in range(20):
#     print('10')


# Даны два числа a и b. Составить программу вывода на экран всех чисел от a до b.

# a = 20
# b = 45
# for i in range(a, b + 1):
#     print(i)


# Дано число N. Составьте программу, выводящую на экран кубы чисел от 1 до N в одну строку.
# N = int(input("enter N:"))
# for i in range(1, N + 1):
#          print(i ** 3, "", end="")

# Выведите на экран в одну строку числа от 100 до -100 включительно.
# for i in range(100, -100, -1):
#     print(i, "", end="")


# Необходимо вывести все четные числа на отрезке [a;a*10].

# a = int(input("Enter a:"))
# for i in range(a, a*10 + 1):
#     if i % 2 == 0:
#         print(i)

#Найти сумму всех целых чисел от 100 до 500 включительно.
# summa = 0
# for i in range(100, 501):
#     summa = summa + i
#     print(summa)


# Найти произведение всех целых числе от 5 до 20 включительно.

# multiply = 1
# for i in range(5, 21):
#     multiply = multiply * i
#     print(multiply)

# Натуральнон число n. Вывести на экран факториал этого числа.

# n = int(input())
# f = 1
# for i in range(2, n + 1):
#     f = f * i
#     print(f)


#  # 9) Текст с пробелами. Написать программу, определяющую количество слов, заканчивающиеся одной и той же буквой.
# s = "kjhg lihih lh"
# s1 = ""
# count = 0
# for i in range(int(len(s))):
#     if s[i] != '':
#         s1 = s1 + s[i]................

#	Дано число n. Вывести все числа от 1 до n.
# n = int(input())
# for i in range(1, n + 1):
#     print(i)


#Дано число n. Посчитать сумму всех чётных чисел от 0 до n.
# n = int(input("enter n:"))
# summa = 0
# for i in range(0, n + 1, 2):
#     summa = summa + i
#     if i % 2 == 0:
#         print(summa)


# # Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0
# n = int(input())
# multiply = 1
# while n > 0:
#     if (n % 10) % 2 == 0:
#         multiply *= (n % 10)
#     n //= 10
# print(multiply)

# Дано число n. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше n.
# n = int(input('Sample Input :'))
# arr = [1, 4, 9, 16, 25, 36]
# for i in arr:
#     if i < n:
#         print('Sample Output :' i, end = " ")


# # Дано число n. Среди чисел 1, 4, 9, 16, 25, ... найти первое, которые больше n.
# n = int(input('Sample Input :'))
# arr = [1, 4, 9, 16, 25]
# for i in arr:
#     if i > n:
#         print('Sample Output :', i)
#         break

# Дано число n. Определить первую цифру этого числа.
# n = int(input())
# while n > 9:
#     n = n // 10
# print(n)

#Дано число n. Найти сумму цифр в этом числе.
# n = int(input())
# summa = 0
# while n > 0:
#     i = n % 10
#     summa = summa + i
#     n = n // 10
# print("Сумма:", summa)


# Дано натуральное число n. Найти значение минимальной цифры в данном числе.
# print(min(list(input())))

# n = int(input())
# # min = 10
# # while n:
# #     i = n % 10
# #     if i < min:
# #         min = i
# #         n = n // 10
# #         print(min)

# Дана непустая последовательность натуральных чисел(вводим с клавиатуры в цикле while через int(input())),
# оканчивающаяся отрицательным числом. Найти максимальное число в данной последовательности



# 1.	Дано натуральное число n < 10. Напишите программу, которая выводит таблицу умножения на n.
# n = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f'{n} * {i} = {n * i}')

# 2.	Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
# multiply = 1
# for i in range(1, 11):
#     print(i)
#     multiply *= i
# print(multiply)


#3.	Дано натуральное число n. Напишите программу, которая печатает численный треугольник/
# n = int(input('Введите число: '))
# for i in range(1, n + 1):
#     print(str(i) * i)


# 4.	Пользователь вводит трехзначное число. Программа должна сложить цифры, из которых состоит это число.
# number = int(input())
# a = number % 10
# b = number // 10 % 10
# c = number // 100
# print(a + b + c)


# 6.	На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, которая находит все простые числа от a до b включительно.
# a = int(input("ВВедите число a: "))
# b = int(input("ВВедите число b: "))
# for i in range(a, b + 1):
#     print(i)

#10.	Получить 100 первых простых чисел.
# for i in range(1, 1000):
#     count = 0
#     number = 2
#     while number < i:
#         if i % number == 0:
#             count += 1
#         number += 1
#     if count == 0:
#         print(f'{i}')

# # 9.	Дан текст. Написать программу, вставляющую после каждой запятой по одному пробелу.
# # Если в тексте встречается два и более пробелов, требуется оставить один.
# s = "Hello, world! Hello, Python, Paskal,C!"
# s += " "
# s1 = ""
# for i in range(len(s)):
#     if s[i] != " ":
#         s1 += s[i]
#     elif s[i] == "," and len(s1) >= 1:
#        print(s1)

# #С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 цифры.
#
# n = int(input("Семизначное число: "))
# number = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
#           n % 10]
# x = 0
# y = 0
# for i in number:  # пробегаемся по списку и считаем четные и нечетные цифры
#     if i % 2 == 0:
#         x += 1
#     else:
#         y += 1
#         print(i)
#         if x > y:
#     print(sum(number))
#     else:
#     print(number[0] * number[2] * number[5])


# 2. С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.


# 3. Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
# Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
# рандомной пары. Проверку выполнить 7 раз.
# В случае равенства (количества, когда пара больше и всех остальных случаем)
# вывести случайные числа, полученные в 4 итерации.


# # 4. Посчитать, сколько раз встречается определенная цифра в числах. Количество
# # введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# # рандомно.
#
# n = int(input("Сколько чисел: "))
# x = int(input("Искомая цифра: "))
# count = 0
# for i in range(1, n + 1):
#     y = int(input("Ввести число " + str(i) + ": "))
#     while y > 0:
#         if y % 10 == x:
#             count += 1
#         y = y // 10
#         print("Было введено %x цифр %x" % (count, x))

# 5. Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран. Строка
# может содержать пробелы.

# s = input()
# x = len(s)
# number = []
# i = 0
# while i < x:
#     s_int = ''
#     y = s[i]
#     while '0' <= y <= '9':
#         s_int += y
#         i += 1
#         if i < x:
#             y = s[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         number.append(int(s_int))
# print(number)


# 6. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных.

# l = input("")
# dubl_lower = 0
# dubl_upper = 0
# for i in range(1, len(l)):
#     print(l[i - 1], l[i])
#     if l[i - 1].islower() and l[i].islower():
#         dubl_lower += 1
#     if l[i - 1].isupper() and l[i].isupper():
#         dubl_upper += 1
# print('В верхнем регистре:', dubl_upper)
# print('В нижнем регистра:', dubl_lower)



# n = int(input())
# number = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
#            n % 10]
# x = 0
# y = 0
#
# for i in number:
#     if i % 2 == 0:
#         x += 1
#     else:
#         y += 1
#
# if x > y:
#     print(sum(number))
# else:
#     print(number[0] * number[2] * number[5])

# a = [4, 6, 'py', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
# a.extend(b)
# print(a)

#                                        Task8

#Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
# my_list = [1, 5, 90, 33, 328]
# for i in my_list:
#     if i % 2 == 0:
#         print(i)

#Задано два списка. Найти наименьшие среди элементов первого списка, которые не входят во второй список.
# a = [165, 68, 37, 9, 6521, 5541]
# b = [632, 41, 4, 8921, 45964, 68, 165]
# a.sort()
# b.sort()
# print(a)
# print(b)
# print("Наименьшее первого списка", a[0])
# print("Наименьшее второго списка", b[0])
# if a[0] not in [b]:
#     print(a[0])

# 3.	Задан список из k чисел.
# # Определить количество инверсий в списке (т. е. таких пар элементов, в которых большее число находится слева от меньшего).

# k = input()
# ivers = 0
# for i in range(len(k)):
#     if k[i] = ab:
#     print(elements.count(x))
# for i in range(len(k)):
#     for j in range(i + 1, len(k)):
#         if k[i] > k[j]:
#             c += 1
#             print(c)

#Программе подаётся на вход произвольная строка. Удалите из нее повторяющиеся символы
# (т. е. символы, встречающиеся в строке во второй или более раз) и выведите результат на экран.
# Задачу решить через список. Функцию set не использовать

# s = input()
# s1 = []
# for i in s1:
#     if i not in s1
#         s1.append(i)
# print(s1)
#print(''.join(s1))


# s = input()
# s_1 = []
# for i in s:
#     if i not in s_1:
#         s_1.append(i)
# print(''.join(s_1))
# # Сгенерировать список нечётных двузначных  чисел.
# lst = [i for i in range(11, 100) if i % 2 != 0]
# print(lst)

# 2.	Сгенерировать список из 10 чисел степени 2. От 1 до 10.
# lst = [i ** 2 for i in range(10)]
# print(lst)
#
# # 3.	Сгенерировать список всех трёхзначных чисел кратных 5 и 3.
# # lst = [i for i in range(100,1000) if i % 5 == 0 and i % 3 == 0]
# # print(lst)
#
# # Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов. Set не использовать.
# lst = [i for i in range(2, 101) if i % i == 0 and i % 1 == 0]
# print(lst)
#
# Дан список состоящий из слов. Отсортировать его по количеству вхождений буквы 'a'
# lst = ["june", "july", "august"]
# str = "".join(lst)
# print(str)
# symbol = input()
# count = 0
# for i in range(len(str)):
#     if str[i] == symbol:
#         count += 1
# # print(count)
#
#
# lst = ["7", "54", "55", "2"]
# str = "0".join(lst)
# print(str)
#
# Даны два кортежа:
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран ( Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих
# кортежей
# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# if sum(A) > sum (B):
#     print("A>")
# else:
#     print("B>")
# min1 = min(A)
# min2 = min(B)
# print(A.index(min1))
# print(B.index(min2))
#
# Создайте  кортеж с цифрами от 0 до 9 и посчитайте сумму
# import random
# tup = tuple([random.randint(1,10)] for i in range(10))
# print(tup)
# sum_tup = 0
# i for in tup
#     print("tup")
#     for i in tup:
#         print(i, end=" ")
#     for i in range(5):
#         sum = sum + tup[i]
#     print("\n Сумма элементов кортежа = ", sum)


# Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,
# 	         'и', 'и', 'т', 'т', 'а', 'и', 'и',
# 	         'и', 'и', 'и', 'т', 'и’)

# sum_A = 0
# i for in A
#     print("A")
#     for i in korteg:
#         print(i, end=" ")
#     for i in range(5):
#         sum = sum + korteg[i]
#     print("\n Сумма элементов кортежа = ", sum)
#
# # # 1.	Дан кортеж. Вывести все его совершенные числа.
# tup = (5, 28, 55, 496, 999)
# lst = [i for i in range(11, 100) if i % 2 != 0]
#
# # #Элементы кортежа числа и строки. Все строки в кортеже сделать перевёртышами, а числа умножить на два.
# tup = (5, 28, 55, 496, 999)
# for i in range(len(tup)):
#     x = 0
#     for j in range(len(1, int(i // 2) + 1):
#         if i % j == 0:
#     x += j
#     if x == i:
#         print(i)

# #2.	Элементы кортежа числа и строки. Все строки в кортеже сделать перевёртышами а числа умножить на два.
# tup = ("Vasya", "45", "Pupkin", "52")
# for elem in range(len(tup)):
#     print(tup[elem])
# #     if int in tup:
# #         print(elem)
# #
# tup = ("Vasya", "45", "Pupkin", "52")
# # for a in tup:
# #     if not a.isalpha():
# #         print(a, end=" ")
# #
# #          *2
#
#
# for b in tup:
#     if b.isalpha():
#         print(b.reverse(), end=" ")
# Дан кортеж. Найти максимальную по длине монотонную последовательность( убывающую или возрастающую) чисел. (5,2,6,8,9,7,5,7,8)

# tup = (5, 2, 6, 8, 9, 7, 5, 7, 8)
# a = min(tup)
# print(a)
# b = max(tup)
# print(b)
# index = tup.index(a)
# print(index)
# index1 = tup.index(b)
# print(index1)
# print(tup [1:5])
#
# # 4.	Дан кортеж. Найти разность между его максимальным и минимальный элементом.
# tup = (5, 2, 6, 8, 9, 7, 5, 7, 8)
# a = min(tup)
# print(a)
# b = max(tup)
# print(b)
# print(b-a)
#6.	Ввести список с клавиатуры. Список преобразовать в кортеж. Посчитать количество элементов между максимальным и минимальным. (5,2,8,9,6,8,3,4) 1 элемент
# sp = [5, 8, 999, 558, 4, 50]
# tup = tuple(sp)
# print(tup)
# print('max', max(tup), 'min', min(tup))
# index = tup.index(max(tup))
# print('index max', index)
# index1 = tup.index(min(tup))
# print('index min', index1)
# # # count...???
#
# # Дан кортеж. Вывести на экран все простые числа в данном кортеже.
# a = (5, 5.6, 46, 53, -6, 100, 0)
# print(a)
# for num in a:
#     if num > 0 and num % num == 0:
#         print(num)

#10.	Дан кортеж. Посчитать сумму элементов между максимальным и минимальным не включая эти элементы. (1,5,2,8,9,6,8,3,4) sum= 15
# tup = (2, 14, 13, 6, 33, 10, 1)
# a = min(tup)
# b = max(tup)
# print('max', max(tup), 'min', min(tup))
# index = tup.index(max(tup))
# print('index max', index)
# index1 = tup.index(min(tup))
# print('index min', index1)
# #s_tup = sum (count...)
#
# # car = {'BMW': ['3', '6', '7'], 'Tesla': ['s', 'x', 'y']}
# # print(car [BMW (0,-1)],
#  d = {'1': '1', '8': '11111111', '2': '11}
#  print (d.key)
#
# product = {
#     "melon": [200, 6.22],
#     "water": [500, 5.52],
#     "apple": [100, 6.21],
#     "cheese": [5, 52.52],
#     'butter': [20, 3.61]
# }
# summa = 0
# while True:
#     name_product = input("enter name product or exit:")
#     if name_product == "exit":
#         break
#     if name_product in product:
#         print('yes')
#     else:
#         print(f"no product name {name_product}")
#
# print(summa)



# 1.	Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество учащихся в разных 9 классах (9а, 9б, 9в, 9м, 9ф и т. п.).
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
# б) в школе появился новый класс.
# в) в школе был расформирован (удален) другой класс.
# г) Вычислите общее количество учащихся 9 классов в школе.
#
# school = {"9а": 19, "9б": 20, "9в": 24, "9м": 25, "9ф": 22, "9я": 21}
# school["9г"] = 20
# del school["9ф"]
# print(f"Всего учеников в школе: {sum(school.values())}")

# 2.	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для введённого слова вывести его синоним или написать что его нет.
#d = {'cola': pepsi, 'brod': bun, 'rice': groats}
# n = int(input())
# dict = {}
# for i in range(n):
#     x, y = map(str, input().split())
#     dict[x] = y
#     dict[y] = x
# y = str(input())
# # print(dict[y])
# 4.	Коля устал запоминать телефонные номера и заказал у Вас программу, которая заменила бы ему телефонную книгу.
# Коля может послать программе два вида запросов: строку, содержащую имя контакта и его номер, разделенные пробелом, или просто имя контакта.
# В первом случае программа должна добавить в книгу новый номер, во втором – вывести номер контакта.
# Ввод происходит до символа точки. Если введенное имя уже содержится в списке контактов, необходимо перезаписать номер.
# put your python code here
# n='' #инициализация строки
# n = str(input())
# m = [] #инициализация списка
# m.append([str(s.lower()) for s in n.split()])
# d = {} #инициализация пустого словаря
# li, lj = len(m), len(m[0])
# for i in range(li):
#     for j in range(lj):
#         p = m[i][j]
#         if p in d:
#             d[p]+=1
#         else:
#             d[p] = 1
# for key,value in d.items():
#    print(key,value)
# put your python code here
# n = ''  # инициализация строки
# n = str(input())
# m = []  # инициализация списка
# m.append([str(s.lower()) for s in n.split()])
# d = {}  # инициализация пустого словаря
# li, lj = len(m), len(m[0])
# for i in range(li):
#     for j in range(lj):
#         p = m[i][j]
#         if p in d:
#             d[p] += 1
#         else:
#             d[p] = 1
# for key, value in d.items():
#     print(key, value)
# d = {'1':a, '2':b}
# print(d)
#
# 1.	Дан список чисел. Определите, сколько в нем встречается различных чисел.
# list = [0, 5, -6, 18, 408, 0.5, -6]
# list2 = set(list)
# elem = len(list2)
# print(elem)

#2.	Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
# a = [5, 58, -4]
# b = [1, 55, -4, 1]
# elem = len(a+b)
# print(elem)

#3.	Даны два списка чисел. Найдите все числа, которые не содержатся одновременно в этих двух списках
# a = [5, 58, 963, 0.7, -6.8, -6]
# b = [0, 5, -6, 18, 408, 0.5]
# a1 = set(a)
# b1 = set(b)
# print(a1-b1)
# print(b1-a1)
# #1.	Сгенерировать двумерный список. Среди строк заданной матрицы, содержащих только нечетные элементы,
# # найти строку с максимальной по модулю суммой элементов.
# lst = [[int(i%2!=0) for i in input().split()] for i in range()]
#
# N = int(input('Введите M: '))
# M = int(input('Введите N: '))
# A = [[0] * M for i in range(N)]
# for i in range(N):
#     for j in range(M):
#         A[i][j] = random.randrange()
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j], end=' ')
#     print()
#     number_row = -1
#     flag = False
#     max_count = 0
#     for i in range(len(A)):
#         count = 0
#         for j in range(len(A[i])):
#             if A[i][j] % 2 != 0:
#                 count += 1
#         if count > max_count:
#             flag = True
#             max_count = count
#             number_row = i
#     if flag:
#         print(number_row)
# # 3.	Дано нечетное число n. Создайте двумерный список из n×n элементов, заполнив его символами "." (каждый элемент списка является строкой из одного символа).
# # Затем заполните символами "*" среднюю строку списка, средний столбец массива, главную диагональ и побочную диагональ.
# # В результате  в списке должна получиться снежинка. Выведите полученный список на экран, разделяя элементы списка пробелами.
# n = int(input())
# a = [['.'] * n for i in range(n)]
# for i in range(n):
#     a[i][i] = '*'
#     a[n // 2][i] = '*'
#     a[i][n // 2] = '*'
#     a[i][n - i - 1] = '*'
# for row in a:
#     print(' '.join(row))
#4.	Даны два числа n и m. Создайте двумерный список размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
# n, m = [int(i) for i in input().split()]
# a = []
# for i in range(n):
#     a.append([])
#     for j in range(m):
#         if (i + j) % 2 == 0:
#             a[i].append('.')
#         else:
#             a[i].append('*')
# for row in a:
#     print(' '.join(row))
#f.write('str'("ФИО") + '\n'' )
# Дана строка. Пользователь ищет в ней подстроку. Если подстрока не найдена то бросьте ValueError.
# s = input()
# substring = input()
# if substring not in s:
#     raise NameError("no substring in string")
# Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали
#try:
#     x = (1, 2, 5, 7)
#     x = x/2
#     print(x)
# except TypeError:
#     print("Type error ;(")
# Дана строка. Проверьте есть ли в ней цифры, иначе бросьте ValueError.
# s = input()
# print(s.isalpha())
# if s.isalpha() == False:
#     raise NameError("figures available")
#16.	Выведите таблицу размером n×n, заполненную числами от 1 до n*n “змейкой”,
# выходящей из левого верхнего угла, как показано в примере (здесь n=5)
# n = int(input())  # размер матрицы
# a = [[0] * n for i in range(n)]  # создание матрицы нужного размера, заполнена 0
# count = 0  # количество заполненных ячеек
# for i in range(n):  # заполнение 1 строки
#     count += 1
#     a[0][i] = count
# j = 0  # указываем последнюю заполненную ячейку
# i = n - 1
# n -= 1  # устанавливаем размер 1 блока 1 витка
# while len(a) ** 2 != count:  # условие выхода из цикла
#     for k in range(n):  # движение вниз
#         j += 1
#         count += 1
#         a[j][i] = count  # заполнение матрицы
#     for k in range(n):  # движение влево
#         i -= 1
#         count += 1
#         a[0][n] = count
#     for k in range(n - 1):  # движение вправо
#         i += 1
#         count += 1
#         a[j][i] = count
#     n -= 2  # обеспечиваем переход на внутренний виток
# for i in range(len(a)):  # вывод полученной матрицы
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()
# n = int(input())
# a = (1, 1 + n0
# print (a)  print("No")
# for i in range(1, 1 + n):
#     a.append([int(j) for j in input().split()])
#     if a % 2 != 0:
#         a.revers()
#         print(a)
# # n = int(input())
# # count_colum = 5
# # for i in range(1, 1+n):
# #
# # #     print(i)
# n = int(input())
# n_1=n
# result = 0
#
# while(n!=0):
#     n1 = n%10
#     result = result*10 + n1
#     n=int(n/10)
#
# print("yes")
# if result==n_1:
#     print("Palindrome!")
# # else:
# n = int(str(input()))
# num_test = n[::-1]
# if n == num_test:
#     print("Yes")
# else:
#     print("NO")
# import random
# N = int(input('Введите M: '))
# M = int(input('Введите N: '))
# A = [[0] * M for i in range(N)]
# for i in range(N):
#     for j in range(M):
#         A[i][j] = random.randrange(1, 100)
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j], end=' ')
#     print()
#     number_row = -1
#     flag = False
#     max_sum = 0
#     for i in range(len(A)):
#         summa = 0
#         for j in range(len(A[i])):
#             if max_sum += summa(len(A[i])):
#                 summa += 1
#         if summa > max_sum:
#             flag = True
#             max_sum = summa
#             number_row = i
#     if flag:
#         print(number_row)
# Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента, которого нет в списке.
# mylist = ['4', 'j', 1, '12', '5', 1.1]
# try:
#     print(mylist.index(6))
# except IndexError:
#     print("IndexError")
# Напишите программу которые будет ловить TypeError, когда вы пытаетесь скаткатенировать строку и число.
# S1 = 'spam'
# x = 1
# try:
#     print(s1+x)
# except TypeError:
#     print(TypeError)
#Напишите программу которая вычисляет площадь треугольника по формуле Герона,
# однако если пользователь введёт длину хоть одной стороны треугольника равную 0,
# то программа должна бросить исключение ArithmeticError.
# try:
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a + b + c) / 2
#     s = (p*(p - a)*(p - b)*(p - c)) ** 0.5
#     if int(0)
# except ArithmeticError:
# # print(ArithmeticError)
# Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError,
# когда пользователь пытается удалить элемент которого нет в списке.
# inp_lst = ['Python','Java','Kotlin','Machine Learning','Keras']
# try:
#     lst.remove(one)
# except TypeError:
# print("TypeError")

# Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры.
# fname = input('Файл: ')
# f = open(fname, 'w')
# while True:
#     s = input()
#     if s == '':
#         break
#     f.write(s + '\n')
# f.close()
# 2. записать три новые строки текста. Записываемые строки вводятся с клавиатуры.
# f = open('test.txt', 'a')
# while True:
#     s = input()
#     if s == '':
#         break
#     f.write(s + '\n')
# f.close()
# #4.	Дан текстовый файл. Подсчитать количество символов в нем.
# # Без \n
#
# for line in open ('test.txt').readlines():
#     print(len(line), end="")
# Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
# # этих кортежей
# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# print("sum of C_1 :", sum(C_1))
# print("sum of C_2:", sum(C_2))
# if sum(C_1) > sum(C_2):
#     print("Сумма больше в кортеже - C_1")
# else:
#     print("Сумма больше в кортеже - C_2")
#     print("Номер минимального элемента кортежа C_1:", C_1.index(min(C_1)) + 1)
#     print("Номер максимального элемента кортежа C_1:", C_1.index(max(C_1)) + 1)
# print("Номер минимального элемента кортежа C_2:", C_2.index(min(C_2)) + 1)
# print("Номер максимального элемента кортежа C_2:", C_2.index(max(C_2)) + 1)
# оздайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.Для решения данной задачи воспользуемся функцией count(),
# которая считает количество вхождений элемента в строку.
# Для генерации словаря воспользуемся синтаксисом представления словарей (dictionary comprehention).
# str1 = 'pythonist'
# my_dict = {i: str1.count(i) for i in str1}
# print(my_dict)
# # Результат:
# {'p': 1, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 'i': 1, 's': 1}
# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку
# str = ' An apple a day keeps the doctor away'
# my_dict = {i: str.count(i) for i in str}
# print(my_dict)
# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
# # первом списке, так и во втором.
# a = [5, 2, 85, 45, -5, 6]
# b= [35, 78, 21, 37, 2, 98]
# # elem = len(a+b)
# # print(elem)
# # В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# # оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# # # баллов и посчитать средний балл по классу
# #
# Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# # списке.
# list1 = [35, 78, 21, 37, 2, 98, 2, 35]
# list2 = []
# for item in list1:
#     if item not in list2:
#         list2.append(item)
# print(list2)
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# a = [35, 78, 21, 37, 2, 98, 2, 35, 98]
# count = 0
# a = [int(i) for i in a]
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             count += 1
# # print(count)
# # Напишите программу, демонстрирующую работу try\except\finally
# f = open('test.txt')
# text = []
# try:
#     for line in f:
#         text.append(int(line))
# except ValueError:
#     print('not zero')
# except Exception:
#     print('?')
# else:
#     print('ok')
# finally:
#     f.close()
# # print('close the file')
# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и
# т.д.). Значение – список, который содержит состав, цену (за 100гр) и кол-во (в
# граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания
# Имеется текстовый файл, содержащий 5 строк.
# Переписать каждую из его строк в список в том же порядке.
# f = open('test2.txt', 'w', encoding='utf-8')
# s1 = input()
# s2 = input()
# s3 = input()
# s4 = input()
# s5 = input()
# f.write(s1+s2+s3+s4+s5)
# f.close()
# Имеется текстовый файл. Получить текст, в котором
# в конце каждой строки из заданного файла добавлен
# восклицательный знак.
# lst = ["Book Thief", "Harry Potter and the Philosopher's Stone", "Rich Dad Poor Dad", "The Great Gatsby"]
# print("Available books:")
# print(lst)
# # Accessing Index of the List Element
# x = lst.index('Book Thief')
# print("Book index- ", x)
# #6.	Имеется текстовый файл.
# -Найти длину самой длинной строки.
# -Найти номер самой длинной строки. Если таких строк несколько, то найти номер одной из них.
# -Напечатать самую длинную строку. Если таких строк несколько, то напечатать первую из них.
# open("asdas.txt", 'r')
#     max_len = 0
#     max_ind = 0
#     str_max = ""
#     ind = 1
#     for line in f:
#         line = line.rstrip()
#         if len(line) > max_len:
#             str_max = line[:]
#             max_ind = ind
#             max_len = len(line)
#         ind += 1
# print(max_len)
# print(max_ind)
# print(str_max)
#Создать файл input.txt и записать в него 10 чисел через пробел.
# Считать из него эти числа.
# Затем записать их произведение в файл output.txt.
# with open("asdas.txt", 'r') as f:
#     for line in f:
#         line = line.rstrip()
# print(f_1)
# Ведомость студентов, сдававших сессию, содержит ФИО и оценки по четырем предметам.
# Вывести список студентов, сдавших сессию со средним баллом больше 7.
# Ведомость студентов, сдававших сессию, содержит ФИО и оценки по четырем предметам.
# Вывести список студентов,
# сдавших сессию со средним баллом больше 7.
# students = {}
# with open('one 1.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         space = line.index(":")
#         key = line[:space]
#         value = line[space + 1:].rstrip().split()
#         value = list(map(int, value))
#         students[key] = value
# print(students)
# for key,value in students.items():
#     summa = sum(value)
#     avg = summa / len(value)
#     value.append(avg)
#     if avg > 7:
#         print(key)
#В файле записаны в столбик целые числа.
#тсортировать их по возрастанию суммы цифр и записать в другой файл.
# 61
# 8
# 45
# 10
# f = open('numbers.txt', "r", encoding='utf-8')
# lst = f.read().splitlines()
# print(lst)
# def listsum(lst):
#    if len(lst) == 1:
#         return lst [0]
#    else:
#         return lst [0] + listsum(lst[1:])
# print(listsum(len[lst]))
#
# lst.sort(sum)
# print(lst)
# f = open('numbers.txt', "r", encoding='utf-8')
# f1 = open("numbers_1.txt",'w')
# f.writelines(f1.readlines(lst))
# 9.	Создать файл input.txt и записать в него 10 чисел через пробел.
# # Считать из него эти числа. Затем записать их произведение в файл output.txt.
# with open("numbers.txt", 'r',encoding='utf-8') as f:
#     for line in f:
#         line = line.rstrip()
# print(line)
# n = 10
# mul = 1
# for i in range(1, n + 1):
#     x = int(input('Введите число: '))
#     mul *= x
# print('Произведение 10 введенных чисел равно: ' + str(mul))
# with open("numbers_1.txt", 'r',encoding='utf-8') as f:
#     for line in f:
#         str(mul)
#Получить текст, в котором в конце каждой строки из заданного файла добавлен восклицательный знак.
# with open('vgmf.txt', 'w', encoding='utf-8') as f:
#     str_elem = 0
#     for line in f:
#         line = line.rstrip()
#         if line[-1] == '!':
#             str_elem = line[:]
# print(str_elem)
#Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
# list1 = [5, 2, 85, 78, 45, -5, 6]
# list2 = [35, 78, 21, 37, 2, 98, 6, 6]
# a = set(list1)
# b = set(list2)
# print(len(a & b))
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# list = [45, 2, 45, 78, 45, 0, -5, 6, 45, 0, 78, 2]
# for i in range(len(list)):
#     if list.index(list[i]) == i:
#         print(list[i], '-', list.count(list[i])//2, 'пар(-а/-ы)')
print("hello")