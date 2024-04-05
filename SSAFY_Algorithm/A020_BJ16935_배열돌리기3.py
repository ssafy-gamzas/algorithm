import sys

input = sys.stdin.readline

N, M, R = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]


def topDown():
    global arr
    ans = [[0] * M for _ in range(N)]
    for i in range(M):
        tmp = []
        for j in range(N):
            tmp.append(arr[j][i])
        tmp = list(reversed(tmp))
        for j in range(N):
            ans[j][i] = tmp[j]

    for a in ans:
        print(*a)
    arr = ans


def leftRight():
    global arr
    for i in range(N):
        arr[i] = list(reversed(arr[i]))
        print(*list(reversed(arr[i])))


def rotateRight():
    global arr
    ans = zip(*arr[::-1])
    for a in ans:
        print(*a)
    arr = ans


def rotateLeft():
    global arr
    ans = list(zip(*arr))[::-1]
    for a in ans:
        print(*a)
    arr = ans


