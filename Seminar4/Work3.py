# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

import random

n = random.randint(0, 99999)
max = n
i = 1
while n != 0:
    n = random.randint(0, 9999999)
    i += 1
    if max < n:
        max = n
print(f'Максимальное число - {max}, было проверено {i} чисел')