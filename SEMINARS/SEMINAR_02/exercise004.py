# найти факториал заданного числа N

number = int(input('Enter your number: '))
fact = 1
n = number
if n > 0:
    while n > 1:
        fact *= n
        n -=1
    print(f'Факториал числа {number} = {fact}')

elif number == 0:
    print(f'Факториал числа {number} = 1')

else:
    print('Вы ввели не корректное число для расчета факториала')

