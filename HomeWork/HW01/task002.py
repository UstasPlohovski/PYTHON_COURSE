# Задача 2: Найдите сумму цифр n-значного числа.
import math

number = int(input('Enter your number: '))
number_size = math.floor(math.log10(number)+1)
# print(number_size)
number_sum = 0
number_temp = 0
for i in range(number_size):
    number_temp = math.floor(((number / math.pow(10,i)))%10)
    number_sum = number_sum + number_temp
print('Summa numbers in your number is: ',number_sum)
