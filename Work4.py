# Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 0, 1, 2, 3

num = int(input('Enter a number to which you want to raise 2 to a power: '))
numPower = 0
i = 0
arrayTwoPower = []
while num > numPower:
    arrayTwoPower.append(i)
    i += 1
    numPower = 2 ** i
print(arrayTwoPower)
