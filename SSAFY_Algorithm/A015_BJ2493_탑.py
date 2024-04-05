import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
top = []
ans = [0]*N

for i in range(N-1, -1, -1):
    now = arr[i]
    if not top:
        top.append([now, i])
    else:
        if now >= top[-1][0]:
            while 1:
                if not top or now < top[-1][0]:
                    break
                ans[top[-1][1]] = i+1
                top.pop()
            top.append([now, i])
        else:
            top.append([now, i])

print(*ans)