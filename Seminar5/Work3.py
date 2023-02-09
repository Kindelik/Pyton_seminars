# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

num = int(input('Enter a number: '))


def prime(number):
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    return 'Простое число' if count < 2 else 'Составное число'


print(prime(num))
