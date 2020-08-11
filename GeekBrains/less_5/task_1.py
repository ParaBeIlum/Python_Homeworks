# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict


enterprises = {}
n = int(input('Введите количество предприятий: '))
summed_profit = 0

for i in range(n):
    name = input('Введите название предприятия: ')
    d = [float(input(f'Введите прибыль за {i} квартал: ')) for i in range(1, 5)]
    enterprises[name] = d[0] + d[1] + d[2] + d[3]
    summed_profit += enterprises[name]

median_profit = summed_profit / n
sorted_enterprises = OrderedDict(sorted(enterprises.items(), key=lambda x: x[1]))
print(f'Средняя прибыль за год предприятий составляет: {median_profit:.2f}')
print(f'Наименования предприятий с прибылью меньше средней: ')

for k, v in sorted_enterprises.items():
    if v < median_profit:
        print(k)

print(f'Наименования предприятий с прибылью больше средней: ')

for k, v in sorted_enterprises.items():
    if v >= median_profit:
        print(k)

print(sorted_enterprises)


