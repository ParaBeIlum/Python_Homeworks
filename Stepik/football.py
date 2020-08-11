n = int(input())
data = [input().split(';') for i in range(n)]
print(data)
result = set()
final_result = {}
for item in data:
    result.add(item[0])
    result.add(item[2])
#Команда:Всего_игр Побед Ничьих Поражений Всего_очков
for key in result:
    final_result[key] = [
    sum(x.count(key) for x in data),
    sum(1 for x in data if ((x[1] > x[3]) and key == x[0]) or ((x[1] < x[3]) and key == x[2])),
    sum(z.count(key) for z in data if (z[1] == z[3])),
    sum(1 for y in data if ((y[1] < y[3]) and key == y[0]) or ((y[1] > y[3]) and key == y[2])),
    0
    ]

for item in final_result:
    print('{!s}:{!s} {!s} {!s} {!s} {!s}'.format(item, final_result[item][0], final_result[item][1],
           final_result[item][2], final_result[item][3], final_result[item][1] *3 + final_result[item][2]))

