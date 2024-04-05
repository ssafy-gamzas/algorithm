from collections import deque

N, K = tuple(map(int, input().split()))

arr = deque([i for i in range(1, N+1)])
print("<", end="")

while arr:
    for _ in range(K-1):
        arr.append(arr.popleft())
    if len(arr) == 1:
        print(arr.popleft(), end=">")
    else:
        print(arr.popleft(), end=", ")

