import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, K, T, M = map(int, sys.stdin.readline().split())
    scores = [[0] * (K + 1) for _ in range(N + 1)]
    submits = [0] * (N + 1)
    last_submit = [0] * (N + 1)

    for i in range(M):
        team, problem, score = map(int, sys.stdin.readline().split())
        if scores[team][problem] < score:
            scores[team][K] += score - scores[team][problem]
            scores[team][problem] = score
        submits[team] += 1
        last_submit[team] = i

    ranking_info = [(scores[i][K], submits[i], last_submit[i], i) for i in range(1, N + 1)]

    ranking_info.sort(key=lambda x: (-x[0], x[1], x[2]))
    # print(ranking_info)
    for i in range(len(ranking_info)):
        if ranking_info[i][3] == T:
            print(i + 1)
            break
