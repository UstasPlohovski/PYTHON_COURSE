# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета

import math

number_ticket = int(input('Enter your number of ticket : '))
number_size = math.floor(math.log10(number_ticket)+1)
print(number_size)

number_sum_first = 0
number_sum_second = 0
number_temp_first = 0
number_temp_second = 0

for i in range(math.ceil(number_size/2)):
    number_temp_first = math.floor(((number_ticket / math.pow(10,i)))%10)
    number_sum_first = number_sum_first + number_temp_first
print('Summa First part is: ',number_sum_first)

for i in range((math.ceil(number_size/2)-1),(number_size)):
    number_temp_second = math.floor(((number_ticket / math.pow(10,i)))%10)
    number_sum_second = number_sum_second + number_temp_second
print('Summa Second part is: ',number_sum_second)

if number_sum_first == number_sum_second:
    print('You are LUCKY!')
else:
    print('Try to buy another ticket...')
