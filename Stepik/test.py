#with open('dataset_3363_2 (4).txt', 'rt') as file:
 #   feed = file.read()[::-1]
feed = 'V2F16z15y8c2F16q9M20E10o12g11J12L16w8t2x10V1Y18w20p12g17n13k18V7W17B12t8a13R3W17b12F4'[::-1]
result = ''
digits = '0123456789'
tmpNumber = ''
number = 0
for i in range(len(feed)):
    if feed[i] not in digits:
        number = int(tmpNumber[::-1])
        result += feed[i] * number
        tmpNumber = ''
    else:
        tmpNumber += feed[i]
print(result[::-1])
#with open('text.txt', 'w') as out:
 #   out.write(result[::-1])