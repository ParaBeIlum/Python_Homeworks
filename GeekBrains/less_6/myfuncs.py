# print(sys.version, sys.platform)
# 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] win32
# type= <class 'str'>, object= __main__ 57
# type= <class 'NoneType'>, object= None 16
# type= <class 'NoneType'>, object= None 16
# type= <class '_frozen_importlib_...'>, object= <_frozen_importlib_...> 48
# type= <class 'NoneType'>, object= None 16
# type= <class 'dict'>, object= {} 64
# type= <class 'module'>, object= <module 'builtins' (built-in)> 72
# type= <class 'str'>, object= C:/Users/biote/PycharmProjects/geekbrains/less_6/1.py 102
# type= <class 'NoneType'>, object= None 16
# type= <class 'function'>, object= <function memory_counter at 0x000001D69E14BB80> 136
# type= <class 'int'>, object= 0 24
# ****************************************
# Размер, занимаемый переменными = 567
# Примерно столько занимает памяти функция и основные служебные процессы, этим значением можно принебречь
# либо вычитать из каждого полученного значения

# В данной реализации попытался учесть тот факт, что различные объекты могут ссылаться на один и тот же объект
# в памяти, для чего в функцию передается пустое множество, которое заполняется по мере работы значениями id переменных,
# в результате занимаемая память учитывается единожды, а ссылки учитываются все.

from sys import getsizeof


def memory_counter(x, ids):
    # print(f'type= {x.__class__}, object= {x}', end=' ')
    if id(x) in ids:
        return 0
    r = getsizeof(x)
    ids.add(id(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            # print(r)
            return r + sum(memory_counter(k, ids) + memory_counter(v, ids) for k, v in x.items())
        if not isinstance(x, str):
            # print(r)
            return r + sum(memory_counter(item, ids) for item in x)
    # print(r)
    return r


def memory_counter2(x):
    sum_mem = 0
    for item in x:
        if item.startswith('__'):
            continue
        elif hasattr(x[item], '__call__'):
            continue
        elif hasattr(x[item], '__loader__'):
            continue
        else:
            sum_mem += getsizeof(x[item])
    return f'Переменные заняли {sum_mem} байт(а)'
