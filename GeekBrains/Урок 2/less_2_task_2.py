# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

num = int(input('Введите натуральное число: '))
evenCount = 0
oddCount = 0
if num == 0:
    evenCount = 1
while num > 0:
    currNum = num % 10
    if currNum % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    num //= 10
print(f'Количество четных цифр в числе: {evenCount}\n'
      f'Количество нечетных цифр в числе: {oddCount}')
