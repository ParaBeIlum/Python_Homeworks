# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parents = [-1] * length
    _start = start
    cost[start] = 0
    min_cost = 0
    way = {}

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):

            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parents[i] = start

        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i, vertex in enumerate(cost):
        if vertex == float('inf'):
            way[i] = 'unreachable'
            continue
        if i == _start:
            way[i] = 0
            continue
        finish = i
        curr_way = deque([finish])
        k = i
        while parents[k] != _start:
            curr_way.appendleft(parents[k])
            k = parents[k]
        curr_way.appendleft(_start)
        way[i] = list(curr_way)

    return f'Длина кратчайшего пути от старта до каждой из вершин:\n' \
           f'{cost}\n' \
           f'Кратчайший путь от старта до каждой из вершин:\n' \
           f'{way}'


s = int(input('Введите стартовую вершину: '))
print(dijkstra(g, s))
