import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))

graph = [deque(map(int, input().split())) for _ in range(N)]
graph2 = deque(deepcopy(graph))

for i in range(1, N):
    graph2[0][i] += graph2[0][i-1]

for i in range(1, N):
    graph2[i][0] += graph2[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        graph2[i][j] = graph2[i-1][j] + graph2[i][j-1] - graph2[i-1][j-1] + graph[i][j]

graph2.appendleft(deque([0]*(N+1)))

for i in range(1, N+1):
    graph2[i].appendleft(0)


for _ in range(M):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    print(graph2[x2][y2] + graph2[x1-1][y1-1] - graph2[x2][y1-1] - graph2[x1-1][y2])

