# Задача №45. Общее обсуждение
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:             Вывод:
# 300               220 284

def divisor_search(num):
    list1 = []
    for i in range(1, num):
        if num % i == 0:
            list1.append(i)
    return sum(list1)


k = int(input("enter k < 10^5 :  "))
setDiv = set()
for i in range(1, k):
    sum_div_i = divisor_search(i)
    if divisor_search(sum_div_i) == i and sum_div_i < k and sum_div_i != i:
        setDiv.add(i)
        setDiv.add(sum_div_i)
print(sorted(list(setDiv)))