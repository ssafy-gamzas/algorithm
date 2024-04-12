import sys

N = int(sys.stdin.readline())
dots = [map(int, sys.stdin.readline().split()) for _ in range(N)]
stack = [(0, 0)]
count = 0
while dots:
    x, y = dots.pop()
    while stack[-1][1] > y:
        stack.pop()

    if stack[-1][1] < y:
        count += 1
        stack.append((x, y))

print(count)
