import sys


def dfs(target, current):
    if chk[current]:
        if target == current:
            answer.append(current)
        return
    chk[current] = True
    dfs(target, numbers[current])


N = int(sys.stdin.readline())
numbers = [0] + [int(sys.stdin.readline()) for _ in range(N)]
answer = []

for idx in range(1, N+1):
    chk = [False] * (N + 1)
    dfs(idx, idx)
print(len(answer))
for a in answer:
    print(a)