# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:                                                  Вывод:
# values = [0, 2, 10, 6]                                  same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(function, values):
    result = list(filter(function, values))
    if len(result) == 0:
        return True
    else:
        return False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
