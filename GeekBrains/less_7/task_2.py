# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

array = [i for i in range(0, 50)]
random.shuffle(array)
print(f'Исходный массив: {array}')


def merge_sort(arr):
    def merge(left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res

    if len(arr) < 2:
        return arr
    else:
        mid = int(len(arr) / 2)
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


print(f'Отсортированный массив: {merge_sort(array)}')
