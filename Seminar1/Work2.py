# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
import math

clasOne = int(input('количество учеников в первом классе - '))
clasTwo = int(input('количество учеников во втором классе - '))
clasThree = int(input('количество учеников в третьем классе - '))

resultClasOne = math.ceil(clasOne/2)
print(resultClasOne)
resultClasTwo = math.ceil(clasTwo/2)
print(resultClasTwo)
resultClasThree = math.ceil(clasThree/2)
print(resultClasThree)
result = resultClasOne + resultClasTwo + resultClasThree
print(result)
