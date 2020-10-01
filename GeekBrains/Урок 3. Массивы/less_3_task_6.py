# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
from myfuncs import memory_counter
import random

size = 1000
array = [random.randint(0, 1000000) for _ in range(size)]
maxI = 0
minI = 0
result = 0
for i, item in enumerate(array):
    if item > array[maxI]:
        maxI = i
    if item < array[minI]:
        minI = i
if maxI > minI:
    for i in range(minI + 1, maxI):
        result += array[i]
elif maxI < minI:
    for i in range(maxI + 1, minI):
        result += array[i]
print(f'Сгенерирован массив случайных чисел\n{array}\n'
      f'Сумма элементов между минимальным и максимальным элементами: {result}')

res = 0
lst = list(locals().copy().values())
for i in lst:
    res += memory_counter(i, set())

print(res)
