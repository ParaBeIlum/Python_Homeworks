# 2. По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y = kx + b, проходящей через эти точки.

print('Введите координаты 2-х точек (х1, у1) и (х2, у2)')
x1 = float(input('х1 = '))
y1 = float(input('у1 = '))
x2 = float(input('х2 = '))
y2 = float(input('у2 = '))
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print(f'Уравнение прямой, проходящей через точки ({x1}, {y1}) и '
      f'({x2}, {y2}), будет иметь вид: y = {k}x + {b}')
