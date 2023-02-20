# def f(x):
#     return x*x
#
# a = f
# print(a(5))
# print(f(5))
#
# def calc1(a,b):
#     return a + b
#
# def calc2(a,b):
#     return a * b
#
# def math(op,a,b):
#     print(op(a,b))
#
#
# math(calc2,5,45)
#
# # calc3 = lambda a,b: a + b
#
# math(lambda a,b: a + b,5,45)
#
# data = [1,2,3,5,8,15,23,38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)
#
# def select (f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
#
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)
#
# list_4 = [x for x in range(1, 20)]
# print(list_4)
#
# list_4 = list(map(lambda x: x + 10, list_4))
# print(list_4)
#
# data_1 = '15 123 45 234 34 56'
# print(data_1)
#
# # data_1 = data_1.split()
# # print(data_1)
#
# data_1 = list(map(int, data_1.split()))
# print(data_1)

# data = '1 2 3 4 5 6 7 8 9'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# users = ['us1', 'us2', 'us3']
# ids = [1, 2, 3]
# data = list(zip(users, ids))
# print(data)

# users = ['us1', 'us2', 'us3']
# data = list(enumerate(users))
# print(data)

# colors = ['red', 'green', 'blue']
# data = open('file_colors.txt', 'a')
# data.writelines(f'{colors}\n')
# data.close()

with open('file_colors.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

path = 'file_colors.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
# режимы открытия файлов:
#   а - открытие и добавление данных
#   r - открытие для чтения данных
#   w - открытие для записис данных (старые данные стираются)
#   w+ - открытие для записи и читать из файла
#   r+ - открывать для чтения и дописывать в него

#  МОДУЛЬ OS:
# import os
# os.chdir(path) - смена текущей директории
# os.getcwd() - текущая рабочая дирректория
# os.path - встроенный модуль в OS
#     os.path.basename(path) - базовое имя пути
#     os.path.abspath(path) - возвращает нормализованный абсолютный путь

# МОДУЛЬ SHUTIL
# import shutil
# shutil.copyfile(src,dst) - копирует содержимое(но не метаданные) файла srs в файл dst
# shutil.copy(src, dst) - копирует содержимое файла src в файол или папку dst
# shutil.rmtree(path) - удаляет текущую дирректорию и все поддиректории; path должне указывать на дирректорию, а не на символическую ссылку