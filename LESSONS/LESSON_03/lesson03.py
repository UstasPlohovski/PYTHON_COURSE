# # сумма чисел от 1 до N
# def sun_number(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
#
# a = sun_number(5, 'qwer')
# print(a)

# # сумма для строки от 1 до N
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
#
# print(sum_str('q', 'w', 'e'))
# print(sum_str('q', 'w', 'e', 'r', 't'))
# print(sum_str('1', '8', '9'))

# МОДУЛЬНОСТЬ

# import moduls
# print(moduls.max(5, 9))

# from moduls import max
# print(max(5, 9))

# from moduls import *
# print(max(5, 9))
#
# import moduls as m
# print(m.max(5, 9))

# РЕКУРСИЯ
# пример вывода чисел фибоначи до 10го значения
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

import moduls
# list_1 = []
# for i in range(1, 10):
#     list_1.append(moduls.fib(i))
# print(list_1)

print(moduls.quick_sort([92,43,5,54,6,34]))

nums = [92,43,5,54,6,34]
moduls.merge_sort(nums)
print(nums)