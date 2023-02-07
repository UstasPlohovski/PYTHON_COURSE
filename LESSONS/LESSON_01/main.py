# a = int(input('Введите число А:'))
# b = int(input('Введите число B:'))
# print(f"{a} + {b} = {a+b}")
# c = a + b

# print(f"{a} + {b} = {c}")

# # print ('hello \"world\"')

# print(a,b,c)
# # print(a,'-'b,'-'c)
# # print('{} - {} - {}'.format(a,,b,c))
# print(f'first - {a} second - {b} third - {c}')

# d = 1>4
# print(d)

# e = 1<4 and 5>2
# print(e)

# f = 1==2
# print(f)

# UserName = input('Введите имя: ')
# if UserName == 'Маша':
#     print('Ура, это же Маша!')
# elif UserName == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif UserName == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', UserName,'!')

# найти сумму всех цифр в числе
# Number = 423
# Summa = 0
# while Summa > 0:
#     x = Number % 10
#     Summa += x
#     Number //=10
# print(Summa)


# i=0
# while i < 5:
#     if i == 3: 
#         break 
#     i=i+1
# else: 
#         print('Пожалуй') 
#         print('хватит )')
# print(i)


# n = 423
# summa = 1
# while summa > 0:
#     x = n % 10
#     summa = summa + x 
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )') 
# print(summa)


# найти минимальный делитель введенного числа
# n = int(input())
# flag = True
# i=2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0 
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False 
#     i += 1

import math
import os
# os.system('cls')

a = int(input('Введите число: '))
print(math.ceil(a/2))
