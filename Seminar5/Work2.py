# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

listX = []
k = random.randint(1, 50)
for i in range(0, k):
    listX.append(random.randint(1, 5))
print(*listX)
for i in range(len(listX)):
     if listX[i] > 3:
        listX[i] = 1
print(*listX)
