# Задача 3: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import time

print('Загадайте 2 числа до 1000 включительно')
time.sleep(2)
sumNumbers = int(input("Введите сумму этих чисел: "))
multNumbers = int(input("Введите произведение этих чисел: "))
x = None
y = None

for i in range(0, 1001):
    temp = sumNumbers - i
    if temp * i == multNumbers:
        x = temp
        y = i
print(f'Вы загадали числа {x} и {y}')
