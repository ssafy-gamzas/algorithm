N = int(input())
M = int(input())
loc = list(map(int, input().split()))
road = [0] * (N + 1)
ans = 0

if M >= 2:
    ans = max(ans, loc[0], N-loc[M-1])  # 처음 가로등과 마지막 가로등의 필수조건
    for i in range(len(loc) - 1):
        if (loc[i+1]-loc[i]) % 2 == 0:
            ans = max(ans, (loc[i+1] - loc[i])//2)
        else:   # 뺀 거리가 홀수면 1 더해줘야함
            ans = max(ans, (loc[i+1] - loc[i])//2+1)
else:
    ans = max(ans, loc[0], N-loc[M-1])
print(ans)

