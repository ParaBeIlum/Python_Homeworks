# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 10
array = [random.randint(0, 100) for _ in range(size)]
print(f'Сгенерирован массив случайных чисел\n{array}')
minVal = array[0]
maxVal = array[0]
for i, item in enumerate(array):
    if item < minVal:
        minVal = item
        minPos = i
    if item > maxVal:
        maxVal = item
        maxPos = i
array[minPos], array[maxPos] = maxVal, minVal
print(f'Поменяем минимальный и максимальный элемент местами\n{array}')
