# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Enter a three-digit number - "))
sumDigits = None
if 99 < number < 1000:
    arrayNumber = list(map(int, str(number)))
    sumDigits = arrayNumber[0] + arrayNumber[1] + arrayNumber[2]
    print(sumDigits)
else:
    print("This number is incorrect")
