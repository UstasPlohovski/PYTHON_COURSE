#   Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с
#  повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#  встречаются в обоих наборах.
#  Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#  элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

size_list1 = int(random.randint(7,10))
print(f'Опеределен размер первого массива = {size_list1}')
list_1 = list()

for i in range(size_list1):
    list_1.append(random.randint(1,10))
print(f'Ваш исходный первый массив: {list_1}')

size_list2 = int(random.randint(5,7))
print(f'Опеределен размер второго массива = {size_list2}')
list_2 = list()

for i in range(size_list2):
    list_2.append(random.randint(1,10))
print(f'Ваш исходный второй массив: {list_2}')

print(set(list_1))
print(set(list_2))

temp_set1 = set(list_1)
temp_set2 = set(list_2)

res = list(filter(lambda x: x in temp_set1, temp_set2))
print(f'Имеются следующие совпадающие значения: {res}')
