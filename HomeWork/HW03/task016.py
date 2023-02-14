# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# Алгоритм:
# 1. Рандомное определение размера массива от 10 до 15
# 2. Рандомное заполнение массива значениями от 0 до 10
# 3. Рандомное определение искомого значания от 0 до 10
# 4. Через цикл проврка на соответствие искомого значения значениям в массива и подстчет
# 5. Вывод результата значения подстчета соответствий

import random

size_list = int(random.randint(10,15))
print(f'You have size list = {size_list}')
list_1 = list()

for i in range(size_list):
    el_list = int(random.randint(1,10))
    list_1.append(el_list)
print(list_1)

number_search = int(random.randint(0,10))
print(f'You have search number  = {number_search}')

count_search = 0
for j in list_1:
    if list_1[j] == number_search:
        count_search +=1
print(f'The Number {number_search} has {count_search} coincidences in this list.')



