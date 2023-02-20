import random

size_garden = int(random.randint(10,15))
print(f'Опеределен размер грядки (кол-во кустов) = {size_garden}')
garden = list()

for i in range(size_garden):
    garden.append(random.randint(10,50))
print(f'Количество и урожайность ваших кустов составляет: {garden}')

res = 0
for i in range(size_garden):
    res_temp = garden[i-1] +garden[(i-2)] + garden[i]
    if res_temp > res:
        res = res_temp
        find_bush = i - 1

print(f'Максимальный урожай с трех кустов {res}')
print(f'Искомый куст {find_bush + 1}')