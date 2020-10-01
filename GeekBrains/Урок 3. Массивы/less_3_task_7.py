# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

size = 10
array = [random.randint(0, 20) for _ in range(size)]
if array[0] > array[1]:
    min1, min2 = 1, 0
else:
    min1, min2 = 0, 1
for i in range(2, size):
    if array[i] < array[min1]:
        spam = min1
        min1 = i
        if array[spam] < array[min2]:
            min2 = spam
    elif array[i] < array[min2]:
        min2 = i
print(f'Сгенерирован массив случайных чисел\n{array}\n'
      f'Элементы с индексами {min1} и {min2} являются минимальными, '
      f'их значения {array[min1]} и {array[min2]}')
