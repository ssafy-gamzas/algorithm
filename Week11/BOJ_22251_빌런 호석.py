N, K, P, X = map(int, input().split())

# N: 1~N층, K: 자리수, P: 반전 최대 개수, X: 멈춰 있는 층수

num = [
    [0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 1, 0, 0, 1, 0],  # 1
    [1, 0, 1, 1, 1, 0, 1],  # 2
    [1, 0, 1, 1, 0, 1, 1],  # 3
    [0, 1, 1, 1, 0, 1, 0],  # 4
    [1, 1, 0, 1, 0, 1, 1],  # 5
    [1, 1, 0, 1, 1, 1, 1],  # 6
    [1, 0, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]


















now = num[X]
ans = 0

def change(index, count):
    global ans

    if count == P:
        ans += 1
        return

    if index == 0:
        for i in range(1, 10):
            if i == X:
                continue
            