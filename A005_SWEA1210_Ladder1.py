from copy import deepcopy

def find():
    global ans
    for s in start:
        tmp = deepcopy(graph)
        init = s
        y = s
        x = 0
        while 1:
            if 0 <= y - 1 < 100 and tmp[x][y-1] == 1:
                tmp[x][y] = 0
                y -= 1
            elif 0 <= y + 1 < 100 and tmp[x][y+1] == 1:
                tmp[x][y] = 0
                y += 1
            else:
                x += 1
            if x == 99:
                if tmp[x][y] == 2:
                    ans = init
                break
        if ans != -1:
            return


for t in range(1, 11):
    a = int(input())
    graph = []
    for _ in range(100):
        graph.append(list(map(int, input().split())))
    start = []
    ans = -1
    # 출발할 수 있는 지점 찾기.
    for i in range(0, 100):
        if graph[0][i] == 1:
            start.append(i)
    find()

    print("#{} {}".format(t, ans))

