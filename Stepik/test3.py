with open('dataset_3363_4 (1).txt') as f:
    text = [line.strip().split(';') for line in f]
sum1 = 0
sum2 = 0
sum3 = 0
for item in text:
    print((int(item[1]) + int(item[2]) + int(item[3])) / 3)
    sum1 += int(item[1])
    sum2 += int(item[2])
    sum3 += int(item[3])

print(sum1 / len(text), sum2 / len(text), sum3 / len(text))
#print(text)

