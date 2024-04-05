from collections import deque

for t in range(1, 11):
    n = int(input())
    arr = deque(list(map(int, input().split())))
    flag = 0
    while not flag:
        for i in range(1, 6):
            tmp = arr.popleft()-i
            if tmp <= 0:
                arr.append(0)
                flag = 1
                break
            else:
                arr.append(tmp)
    print("#{} ".format(t), end="")
    print(*arr)

