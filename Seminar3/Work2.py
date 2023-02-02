# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


listX = [1, 2, 3, 4, 5]
k = 3
lengthX = len(listX)
for i in range(0, k):
    temp = listX[lengthX-1]
    listX.pop(len(listX) - 1)
    listX.insert(0, temp)
print(listX)