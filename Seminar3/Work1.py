# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_x = [1, 1, 2, 0, -1, 3, 4, 4]
newSet = set(list_x)
print(len(newSet))

lengthX = lengthUniq = len(list_x)
for i in range(0,lengthX):
    for j in range(i,lengthX):
        if i == j:
            lengthUniq -=1
print(lengthUniq)