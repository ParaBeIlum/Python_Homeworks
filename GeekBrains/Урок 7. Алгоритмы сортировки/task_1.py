# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Примечания: a. алгоритм сортировки
# должен быть в виде функции, которая принимает на вход массив данных, b. постарайтесь сделать алгоритм умнее,
# но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской,
# шейкерная и другие в зачёт не идут.

import random

array = [i for i in range(-100, 100)]
random.shuffle(array)
array1 = array.copy()


def bubble_sort(arr):
    counter = 0
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            counter += 1
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
        #print(arr)
    return f'Отсортированный массив:\n{arr}\nКоличество проходов: {counter}\n'


# Для усовершенствования алгоритма добавлена проверка на то, были ли в данном проходе перестановки. Также
# запоминается индекс последней перестановки и длина проверяемого массива сокращается не на 1, а идет до данного
# индекса. Также добавил переменные min_position и max_position, которые помогают избавиться от больших значений в
# начале и маленьких в конце. Что позволяет получить почти одну и ту же сложность независимо от входных данных
# (количество проходов сокращается примерно в 2 раза для случайных данных, для отсортированного массива сложность О(n))


def improved_bubble_sort(arr):
    counter = 0
    change_position = len(arr) - 1
    min_position = len(arr) - 1
    max_position = 0
    while min_position >= 0:
        changed = False
        i = max_position
        while i < min_position:
            counter += 1
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change_position = i
                changed = True
            if arr[i] < arr[min_position]:
                arr[i], arr[min_position] = arr[min_position], arr[i]
                changed = True
            if arr[i] > arr[max_position]:
                arr[i], arr[max_position] = arr[max_position], arr[i]
                changed = True

            i += 1
        if not changed:
            return f'Отсортированный массив:\n{arr}\nКоличество проходов: {counter}\n'
        min_position = change_position
        max_position += 1
        #print(arr)
    return f'Отсортированный массив:\n{arr}\nКоличество проходов: {counter}\n'


print(f'Исходный массив:\n{array}')
print(f'Отсортированный массив:\n{bubble_sort(array)}')
print(f'Исходный массив:\n{array1}')
print(f'Отсортированный массив:\n{improved_bubble_sort(array1)}')
