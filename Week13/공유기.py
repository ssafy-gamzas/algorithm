import sys

N, C = map(int, sys.stdin.readline().split())
wifi = sorted([int(sys.stdin.readline()) for _ in range(N)])

start = 1
end = wifi[-1] - wifi[0]
answer = float('-inf')
while start <= end:
    mid = (start + end) // 2
    count = 1
    current = wifi[0]
    for i in range(1, N):
        if current + mid <= wifi[i]:
            count += 1
            current = wifi[i]
    if count < C:
        end = mid - 1

    else:
        answer = max(answer, mid)
        start = mid + 1

print(answer)