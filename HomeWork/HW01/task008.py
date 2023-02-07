# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input('Enter chocolate long (slice): '))
m = int(input('Enter chocolate width (slice): '))
k = int(input('Enter your size slice: '))

if (((k / n) * 10) %10) == 0 or (((k / m) * 10) %10) == 0:
    print('Bon appetit!')
else:
    print('Sorry, try again...')
