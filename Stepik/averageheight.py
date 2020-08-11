# import re
# data = []
# result = {i: [0, 0] for i in range(1, 12)}
# with open('dataset_3380_5 (1).txt', 'r') as f:
#     for line in f:
#         data.append([int(i) for i in re.findall('\d+', line)])
#
# for pupil in data:
#         result[pupil[0]][0] += pupil[1]
#         result[pupil[0]][1] += 1
# for k in result:
#     if result[k][0] == 0:
#         print(k, '-')
#     else:
#         print(k, result[k][0]/result[k][1])
d = {i: [] for i in range(1,12)}
with open('dataset_3380_5 (1).txt', 'r', encoding='utf-8') as f1:
  for i in f1:
    d[int(i.split()[0])].append(float(i.split()[2]))

for i in range(1,12):
  if d[i]:
    print(i, sum(d[i])/len(d[i]))
  else:
    print(i, '-')


print(d)

