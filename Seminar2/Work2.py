# Задача №11. Общее обсуждение
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

number = int(input("Enter a number: "))
fib1 = 0
fib2 = 1
fib_sum = 0
i = 2
while fib_sum < number:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
if fib_sum == number:
    print("Индекс введенного числа", i)
else:
    print(-1)
