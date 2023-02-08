# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Алгоритм:
# 1. Ввод числа N
# 2. Цикл с возведением 2ки в степень k +=1 b печать результата и проверка на не превышение N

import math

n = int(input('Enter any number: N = '))
result = 0
k_temp = 1
while result <= n:
    result = math.pow(2, k_temp)
    if result <= n:
        print(f'{result}; ')
        k_temp +=1
    else:
        print('It is all')
