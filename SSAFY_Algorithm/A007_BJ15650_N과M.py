import sys
from itertools import combinations
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))

for c in combinations([x for x in range(1, N+1)], M):
    print(*c)