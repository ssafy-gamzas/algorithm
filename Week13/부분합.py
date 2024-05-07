import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

front = 0
back = 0
current = 0
answer = float('inf')

while True:
    if current >= S:
        answer = min(answer, back - front)
        current -= nums[front]
        front += 1
    elif back == N:
        break
    else:
        current += nums[back]
        back += 1

if answer == float('inf'):
    print(0)
else:
    print(answer)
