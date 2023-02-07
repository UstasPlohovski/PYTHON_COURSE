# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.Выведите минимальное количество монет, которые нужно перевернуть.
# Алгоритм:
# 1. Определение (ввод) общего количества монет
# 2. Определение (ввод) значения каждой монеты
# 3. Подсчет количества каждого значения монет
# 4. Вывод количества монет с меньшим значением вариантов
#
quantity_coins = int(input('Enter quantity coins: '))
coin = [0]*quantity_coins
for i in range(len(coin)):
    coin[i] = int(input('Enter heads or tails for next coin (0 or 1): '))
quantity_heads = 0
quantity_tails = 0
for i in range(len(coin)):
    if coin[i] == 0:
        quantity_heads += 1
    else:
        quantity_tails += 1
for i in range(len(coin)):
    print(coin[i], end = "; ")
print()
print('Heads =',quantity_heads)
print('Tails =',quantity_tails)

if quantity_heads > quantity_tails:
    print(f'You have to flip {quantity_tails} tails coins')
elif quantity_heads < quantity_tails:
    print(f'You have to flip {quantity_heads} heads coins')
else:
    print(f'Still! You can to flip {quantity_heads} heads or tails coins')