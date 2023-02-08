# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает
# Кате по математике. Он задумывает два натуральных числа X и Y (X, Y≤1000), а Катя должна
# их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Алгоритм:
# 1. Ввод двух задуманных Петей чисел (Х и У)
# 2. Вывод из суммы и произведения для озвучивания Кате
# 3. Решение от обратного через систему уравнений методом подстановки

import math

x = int(input('Enter any first number from 0 till 1000: '))
y = int(input('Enter any second number from 0 till 1000: '))
s = x + y
p = x * y


print(f'Dear Kate, Sum of two numbers = {s} and product of two numbers = {p} ')
print('What numbers did i guess?')

y_kate = int ((s + math.sqrt(math.pow(s, 2) - (p * 4))) / 2)
x_kate = int ((s - math.sqrt(math.pow(s, 2) - (p * 4))) / 2)

print(f'Kate says: You gessed numbers {x_kate} and {y_kate}, my dear brother!')
