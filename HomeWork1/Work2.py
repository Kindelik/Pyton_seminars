# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
import math

numberCranes = int(input('Введите колиичество сделанных журавликов - '))
cranesPetya = math.floor(numberCranes / 6)
cranesSerega = cranesPetya
cranesKatya = (cranesSerega + cranesPetya) * 2
while numberCranes > (cranesKatya + cranesSerega + cranesPetya):   # Костыль, если введенное число не будет кратно 6
    cranesKatya = cranesKatya + 1
print(f'Катя сделала - {cranesKatya}\nПетя сделал - {cranesPetya}\nСережа сделал - {cranesSerega}')
