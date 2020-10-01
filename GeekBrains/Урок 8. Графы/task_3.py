# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины
# связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания: a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from collections import deque
import random

N = int(input('Введите количество вершин: '))
is_visited = [False] * N
parents = [-1] * N
way = {}


def graph_gen(n):
    graph = {_: set() for _ in range(n)}
    for i in range(n - 1):
        graph[i].add(i + 1)
    for i in range(n - 1, 0, -1):
        graph[i].add(i - 1)
        for _ in range(random.randint(0, n)):
            graph[i].add(random.randint(i - 1, n - 1))
        graph[i].discard(i)
    return graph


g = graph_gen(N)
print(f'Сгенерирован список смежности графа:\n{g}')


def in_depth_search(graph, start):
    is_visited[start] = True
    for i in graph[start]:
        if not is_visited[i]:
            parents[i] = start
            in_depth_search(graph, i)


s = int(input('Введите стартовую вершину: '))
in_depth_search(g, s)
print(f'Список родителей для вершин:\n{parents}')

for i, vertex in enumerate(parents):
    if vertex == float('inf'):
        way[i] = 'unreachable'
        continue
    if i == s:
        way[i] = 0
        continue
    finish = i
    curr_way = deque([finish])
    k = i
    while parents[k] != s:
        curr_way.appendleft(parents[k])
        k = parents[k]
    curr_way.appendleft(s)
    way[i] = list(curr_way)

print(f'Путь от старта до каждой из вершин (необязательно кратчайший):\n{way}')
