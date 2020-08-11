# 4. Определить, какое число в массиве встречается чаще всего.
from myfuncs import memory_counter
import random

size = 1000
array = [random.randint(0, 1000) for _ in range(size)]
result = {}
for i in array:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
maxRepeat = 1
for i in result.values():
    if i > maxRepeat:
        maxRepeat = i
print(f'Сгенерирован массив со случайными числами\n{array}\n'
      f'Число повторений каждого из чисел\n{result}\n'
      f'Чаще всего встречаются числа:')
for i in result:
    if result[i] == maxRepeat:
        print(i)

res = 0
lst = list(locals().copy().values())
for i in lst:
    res += memory_counter(i, set())

print(res)