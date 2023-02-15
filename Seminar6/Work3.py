# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:         Вывод:
# 1 2 3 2 3       2
import random

k = random.randint(9, 10)
listK = []
count = 0
for i in range(k):
    listK.append(random.randint(0, k))
print(listK)
for i in range(len(listK)):
    for j in range(len(listK)):
        if listK[i] == listK[j] and i != j and listK[i] != -1 and listK[j] != -1:
            count += 1
            listK[i] = -1
print(count)
