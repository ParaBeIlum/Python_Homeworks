# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

size = 5
a = [[random.randint(0, 10) for _ in range(size)] for _ in range(size)]
for j in range(size):
    minVal = a[0][j]
    for i in range(size):
        if a[i][j] < minVal:
            minVal = a[i][j]
    if j == 0:
        maxVal = minVal
    if minVal >= maxVal:
        maxVal = minVal

for line in a:
    for item in line:
        print(f'{item:>4}', end='')
    print()

print(f'Максимальным элементом среди минимальных элементов столбцов '
      f'матрицы является {maxVal}')
