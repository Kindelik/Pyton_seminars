# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Enter a three-digit number - "))
if 99 < number < 1000:
    arrayNumber = map(int, str(number))
    print(type(arrayNumber))
    # sumDigits = arrayNumber[0] + arrayNumber[1] + arrayNumber[2]
    sumDigits = sum(arrayNumber)
    print(sumDigits)
else:
    print("This number is incorrect")
