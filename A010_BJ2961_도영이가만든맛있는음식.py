import sys
input = sys.stdin.readline

def cook(i, s, b):
    global ans
    if i == N:
        if s != 1 and b != 0:
            ans = min(ans, abs(s-b))
        return

    cook(i+1, s*favor[i][0], b+favor[i][1])
    cook(i+1, s, b)


N = int(input())
favor = []
ans = sys.maxsize

for _ in range(N):
    favor.append(list(map(int, input().split())))

cook(0, 1, 0)

print(ans)