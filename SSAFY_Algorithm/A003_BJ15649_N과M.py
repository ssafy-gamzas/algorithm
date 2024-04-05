import sys
from itertools import permutations
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))

for p in permutations([i for i in range(1, N+1)], M):
    print(*p)