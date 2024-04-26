import sys

input = sys.stdin.readline

N, M = map(int, input().split())
moon = [list(map(int, input().split())) for _ in range(N)]

# 우주선 방향
dx = [1, 1, 1]
dy = [-1, 0, 1]
ans = sys.maxsize


def move(x, y, index, tmp):
    global ans
    for i in range(3):
        if i == index:
            continue
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            tmp += moon[nx][ny]
            if nx == N-1:
                ans = min(ans, tmp)
                return
            move(nx, ny, i, tmp)


for y in range(M):
    start_x = 0
    start_y = y
    fuel = moon[start_x][start_y]
    if fuel == 1:
        move(start_x, start_y, -1, fuel)

print(ans)
