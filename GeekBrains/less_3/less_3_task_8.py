# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

size = 4
a = [[0 for _ in range(size + 1)] for _ in range(size)]
lineSum = 0
for i in range(size):
    for j in range(size):
        a[i][j] = int(input())
        lineSum += a[i][j]
    a[i][size] = lineSum
    lineSum = 0
for line in a:
    for item in line:
        print(f'{item:>4}', end='')
    print()
