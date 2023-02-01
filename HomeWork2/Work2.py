# Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

import random

quantityCoin = int(input('Введите количетсво монет: '))
sideCoin = []
headCoin = 0
tailCoin = 0
for i in range(quantityCoin):
    tempSide = int(random.randint(0, 1))
    sideCoin.insert(i, tempSide)
    if sideCoin[i] > 0:
        headCoin += 1
    else:
        tailCoin += 1
if headCoin > tailCoin:
    print(f'Переверните {tailCoin} монет, которые лежат решкой вверх')
else:
    print(f'Переверните {headCoin} монет, которые лежат орлом вверх')