number = int(input("Введите число, факториал которого, нужно вычислить: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)
