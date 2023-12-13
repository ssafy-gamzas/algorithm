import sys
input = sys.stdin.readline

N, M, R = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N//2, M//2)):
        # print("{} 입니다".format(i))
        x = i
        y = i
        now = arr[x][y]
        for j in range(i+1, N-i):
            # print(j, y)
            next = arr[j][y]
            arr[j][y] = now
            now = next
            x = j
        # print()
        for j in range(i+1, M-i):
            # print(x, j)
            next = arr[x][j]
            arr[x][j] = now
            now = next
            y = j
        # print()
        for j in range(x-1, i-1, -1):
            # print(j, y)
            next = arr[j][y]
            arr[j][y] = now
            now = next
            x = j
        # print()
        for j in range(y-1, i-1, -1):
            # print(x, j)
            next = arr[x][j]
            arr[x][j] = now
            now = next
            y = j
        # print()
for a in arr:
    print(*a)