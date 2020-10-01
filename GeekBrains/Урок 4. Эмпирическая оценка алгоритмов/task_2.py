# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и
# сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
# попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2


import cProfile


def test_prime(func):
    dic = {2: 3, 4: 7, 5: 11, 1: 2}
    for i in dic:
        assert dic[i] == func(i)
        print(f'{i} по счету простое число: {dic[i]}')


def prime(n):
    def is_prime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    counter = 0
    num = 2
    while counter < n:
        if is_prime(num):
            counter += 1
        num += 1
    return num - 1


# test_prime(prime)
# 2 по счету простое число: 3
# 4 по счету простое число: 7
# 5 по счету простое число: 11
# 1 по счету простое число: 2

# cProfile.run('prime(100)')
# 544 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 <string>:1(<module>)
# 1    0.000    0.000    0.001    0.001 task_2.py:29(prime)
# 540  0.000    0.000    0.000    0.000 task_2.py:30(is_prime)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# task_2.prime(10000)
# 5 loops, best of 5: 313 msec per loop

# task_2.prime(100)
# 1000 loops, best of 5: 379 usec per loop

# task_2.prime(1000)
# 1000 loops, best of 5: 10.8 msec per loop

def sieve(n):
    size = n
    primes = [0] * n
    numbers = [0] * size
    for i in range(0, size):
        numbers[i] = i
    primes[0] = 2
    i = 0
    while i < n - 1:
        p = primes[i]
        i += 1
        for j in range(p * 2, size, +p):
            numbers[j] = 0
        while p + 1 < size and numbers[p + 1] == 0:
            p += 1
        if p + 1 >= size:
            tmp = [0] * size * 2
            for k in range(0, size):
                tmp[k] = numbers[k]
            numbers.clear()
            size *= 2
            numbers = tmp
            for j in range(int(size / 2), size):
                numbers[j] = j
            i = 0
        else:
            primes[i] = p + 1
    return primes[n - 1]
    numbers.clear()
    primes.clear()

# test_prime(sieve)
# 2 по счету простое число: 3
# 4 по счету простое число: 7
# 5 по счету простое число: 11
# 1 по счету простое число: 2

# cProfile.run('sieve(100)')
# 7 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 <string>:1(<module>)
# 1    0.001    0.001    0.001    0.001 task_2.py:22(sieve)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 3    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# task_2.sieve(10000)
# 5 loops, best of 5: 173 msec per loop

# task_2.sieve(1000)
# 1000 loops, best of 5: 9.64 msec per loop

# task_2.sieve(100)
# 1000 loops, best of 5: 841 usec per loop

# Вывод: алгоритм с ситом лучше работает с большими числами, имеет меньшую сложность O(n*log(log(n)))
# Алгоритм перебора делителей делает много вложенных вызовов, имеет сложность O(sqrt(n))
