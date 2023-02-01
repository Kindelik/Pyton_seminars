# Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


import array

numWatermelon = int(input('Enter the number of watermelons: '))
maxMass = minMass = int(input('Enter the mass of watermelon №1: '))
for i in range(2, numWatermelon + 1):
    tempMass = int(input(f'Enter the mass of watermelon №{i}: '))
    if tempMass > maxMass:
        maxMass = tempMass
    if tempMass < minMass:
        minMass = tempMass
print('Minimum weight =', minMass)
print('Maximum weight =', maxMass)

# Вариант через список
numWatermelon = int(input('Enter the number of watermelons: '))
massWatemelons = [int(value) for value in input('Enter the mass of watermelons through ,\n ').split(',')]
maxMass = massWatemelons[0]
minMass = massWatemelons[0]
for i in range(1, numWatermelon):
    if massWatemelons[i] > maxMass:
        maxMass = massWatemelons[i]
    if massWatemelons[i] < minMass:
        minMass = massWatemelons[i]
print('Minimum weight =', minMass)
print('Maximum weight =', maxMass)
