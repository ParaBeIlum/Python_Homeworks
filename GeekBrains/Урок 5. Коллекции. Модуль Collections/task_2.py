# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’]. Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому
# использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque

operation = input('Введите 1 для сложения, 2 для умножения двух шестнадцатеричных чисел: ')
one = input('Введите 1 число: ')
two = input('Введите 2 число: ')

hex_nums = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


def hex_sum(a, b):
    result = deque()
    k = 0
    first = deque(a)
    second = deque(b)
    if len(first) > len(second):
        first, second = second, first

    while len(first) > 0:
        spam = hex_nums.index(second.pop())
        egg = hex_nums.index(first.pop())
        result.appendleft(hex_nums[(spam + egg + k) % 16])
        k = (spam + egg) // 16

    while len(second) > 0:
        sec = second.pop()
        result.appendleft(hex_nums[(hex_nums.index(sec) + k) % 16])
        if hex_nums.index(sec) > 15:
            k = 1
        else:
            k = 0
    if k == 1:
        result.appendleft('1')
    return result


def hex_multiply(a, b):
    if a == '0' or b == '0':
        return 0
    first = deque(a)
    second = deque(b)
    result = deque('0')
    _result = deque()
    zero_adder = 0
    if len(first) > len(second):
        first, second = second, first
    while len(first) > 0:
        k = 0
        spam = hex_nums.index(first.pop())
        for i in reversed(second):
            egg = hex_nums.index(i)
            _result.appendleft(hex_nums[(spam * egg + k) % 16])
            k = (spam * egg + k) // 16
        for _ in range(zero_adder):
            _result.append('0')
        if k > 0:
            _result.appendleft(hex_nums[k])
        result = hex_sum(result, _result)
        _result.clear()
        zero_adder += 1
    return result


if operation == '1':
    print(hex_sum(one, two))
    print(f'Проверочка: {hex(int(one, 16) + int(two, 16))}')

if operation == '2':
    print(hex_multiply(one, two))
    print(f'Проверочка: {hex(int(one, 16) * int(two, 16))}')
