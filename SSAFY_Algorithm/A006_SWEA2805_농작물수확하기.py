T = int(input())

for t in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += sum(graph[i][abs(N//2-i):N-abs(N//2-i)])
    print("#{} {}".format(t, ans))
