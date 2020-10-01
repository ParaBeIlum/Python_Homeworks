# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
from myfuncs import memory_counter
import random

size = 1000
array = [random.randint(-100000, 100000) for _ in range(size)]
num = float('-inf')
index = -1
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i
print(f'Сгенерирован массив случайных чисел\n{array}\n'
      f'Максимальный отрицательный элемент: {array[index]}\n'
      f'Его позиция в массиве: {index}')


res = 0
lst = list(locals().copy().values())
for i in lst:
    res += memory_counter(i, set())

print(res)