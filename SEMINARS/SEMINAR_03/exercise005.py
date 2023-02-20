import math
import random
from random import randint
#
# # Преобразование произвольного массива в список только уникальных значений
# my_list = [2,3,4,5,3,5,2,7,5,8,9]
# new_list = list(set(my_list))
#
# print(new_list)
#
# # Заполнение списков
# #     ввод с клавиатуры
# list_1 = list() # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
#     n = int(input()) # пользователь вводит целое число
#     list_1.append(n) # сохранение элемента в конец списка
# print(list_1)

    # генерация случайных значений
# list_2 = list() # создание пустого списка
# for j in range(5): # цикл выполнится 5 раз
#     m = int(random.randint(1,10)) # рандомная генерация целого числа в указанном диапазоне
#     list_2.append(m) # сохранение элемента в конец списка
#     # форматы печати списков
# print(list_2)
# print(*list_2, sep=' ', end='\n')
# print(*list_2, sep='***', end='- теперь другой массив -')

# # СДВИГ ЭЛЕМЕНТОВ В МАССИВЕ на к-позиций.
#
# # вариант 1
# size_list = int(random.randint(7,10))
# print(f'Опеределен размер массива = {size_list}')
# list_1 = list()
#
# for i in range(size_list):
#     el_list = int(random.randint(1,10))
#     list_1.append(el_list)
# print(f'Ваш исходный массив: {list_1}')
#
# k = int(input('Введите на сколько элементов будет сдвиг: '))
#
# while k > 0:
#     list_1.append(list_1[0])
#     list_1.remove(list_1[0])
#     k-=1
# print(list_1)

# вариант 2

# # ЗАДАЧА 21
# # Напишите программу для печати всех уникальных значений в словаре.
# # Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
#
# вариант 1
# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
#
# my_list1 = []
# for i in my_list:
#     for value in i.values():
#         my_list1.append(value)
# print(set(my_list1))
#
# # вариант 2
# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# my_list1 = {set(i.values()).pop().strip() for i in my_list}
# print(my_list1)
# # Задача No23. Общее обсуждение
# # Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# # Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)
#
# def count_large(arr):
#     count = 0
#     for i in range(1,len(arr)):
#         if arr[i] > arr[i-1]:
#             count +=1
#     return count
#
# array = [8, -1, 5, 2, 3]
# print(count_large(array))

# генератор рандомного заполнени списка
my_list = [randint(-10, 10) for _ in range(randint(1,10))]
print(my_list)

my_list1 = [f'{my_list[i]} > {my_list[i-1]}' for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(my_list1)
print(*my_list1, sep='; ')