from collections import deque

for t in range(1, 11):
    n = int(input())
    q = deque(list(map(int, input().split())))
    for _ in range(n):
        q = sorted(q)
        if q[len(q)-1] - q[0] <= 1:
            break
        q[len(q)-1] -= 1
        q[0] += 1
    print("#{} {}".format(t, max(q)-min(q)))
