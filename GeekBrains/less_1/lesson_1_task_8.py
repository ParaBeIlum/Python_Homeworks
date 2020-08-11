# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите 3 разных числа: ')
a = int(input("а = "))
b = int(input("b = "))
c = int(input("c = "))
if a > b:
    mx = a
else:
    mx = b
if c > mx:
    mx = c
if a < b:
    mn = a
else:
    mn = b
if c < mn:
    mn = c
md = a + b + c - mx - mn
print(f'Среднее число: {md}')
