# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

n = int(input())
m = n + n


def rev(n, m):
    print(n + 1)
    if n < m:
        rev(n + 1, m)
    if n == m:
        return


rev(n, m)
