# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы. Примечание: задачу можно решить без сортировки исходного массива. Но если
# это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также
# недопустима).

import random

m = int(input('Введите натуральное число m, будет сгенерирован массив размером 2m + 1: '))
array = [random.randint(0, 50) for i in range(2 * m + 1)]
print(f'Исходный массив: {array}')


def med_finder(arr):
    k = len(array) // 2

    def partition(arr, m):
        left = []
        right = []
        med = []
        for i in arr:
            if i < m:
                left.append(i)
            elif i > m:
                right.append(i)
            else:
                med.append(i)
        return left, right, med

    def med_split(arr, k):
        if len(arr) == 1 and k == 0:
            return arr[0]
        possible_med = arr[0]
        # left = [i for i in arr if i < possible_med]
        # right = [i for i in arr if i > possible_med]
        # med = [i for i in arr if i == possible_med]
        left, right, med = partition(arr, possible_med)
        if k < len(left):
            return med_split(left, k)
        elif k < len(left) + len(med):
            return med[0]
        else:
            return med_split(right, k - len(med) - len(left))

    return med_split(arr, k)


print(f'Медианой является число: {med_finder(array)}')
print(f'Проверочка: {sorted(array)[len(array) // 2]}')
