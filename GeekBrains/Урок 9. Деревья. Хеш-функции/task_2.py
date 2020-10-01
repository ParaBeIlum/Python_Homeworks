# 2. Закодируйте любую строку по алгоритму Хаффмана.

import collections
import heapq


class Node(collections.namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(collections.namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


s = input('Введите строку, которую требуется закодировать: ')

h = []
for ch, freq in collections.Counter(s).items():
    h.append((freq, len(h), Leaf(ch)))
heapq.heapify(h)
count = len(h)
while len(h) > 1:
    freq1, _count1, left = heapq.heappop(h)
    freq2, _count2, right = heapq.heappop(h)
    heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
    count += 1
code = {}
if h:
    [(_freq, _count, root)] = h
    root.walk(code, "")

print(f'Словарь Хаффмана для исходной строки:\n{code}')

print('Закодированная строка: ')
for ch in s:
    print(f'{code[ch]}', end=' ')


# 00 10 10 010 011 00 110 110 010 011 00 10 10 1110 1111
# 0001011001010011011010010100010111101111