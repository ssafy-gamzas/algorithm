import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

# init
for m in range(M):
    for k in range(3):
        dp[0][m][k] = graph[0][m]

for i in range(1, N):
    for j in range(M):
        # 이전에 따라 다음 위치를 업데이트 해줌.
        for k in range(3):
            # 왼쪽 go
            if k == 0:
                if j > 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][1] + graph[i][j], dp[i-1][j-1][2] + graph[i][j])
            # 직진 go
            elif k == 1:
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][0] + graph[i][j], dp[i-1][j][2] + graph[i][j])
            # 오른쪽 go
            else:
                if j < M-1:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j+1][0] + graph[i][j], dp[i-1][j+1][1] + graph[i][j])

answer = float('inf')
for m in range(M):
    for k in range(3):
        answer = min(answer, dp[N-1][m][k])

print(answer)