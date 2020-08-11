# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
from myfuncs import memory_counter
n = int(input('Введите сумму скольки элементов ряда: 1, -0.5, 0.25, -0.125,… '
              'вы хотите получить: '))
result = 0
curr = 1
for i in range(n):
    result += curr
    curr /= -2
print(f'Сумма {n} элементов ряда будет равна: {result}')
res = 0
lst = list(locals().copy().values())
for i in lst:
    res += memory_counter(i, set())

print(res)