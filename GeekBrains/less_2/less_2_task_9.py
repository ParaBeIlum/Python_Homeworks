# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме
# цифр. Вывести на экран это число и сумму его цифр.

# В задании не уточнено насчет варианта, при котором сумма цифр нескольких
# чисел совпадает, например (1111, 4, 22). Будет выведено первое из чисел


def num_digits_sum(num):
    digits_sum = 0
    while num > 0:
        digits_sum += num % 10
        num //= 10
    return digits_sum


n = int(input('Введите количество чисел: '))
sumResult = 0
numResult = 0
print(f'Введите числа, в количестве {n}: ')
for i in range(n):
    num = int(input())
    if num_digits_sum(num) > sumResult:
        sumResult = num_digits_sum(num)
        numResult = num
print(f'Число с наибольшей суммой цифр: {numResult}\n'
      f'Сумма цифр составляет: {sumResult}')
