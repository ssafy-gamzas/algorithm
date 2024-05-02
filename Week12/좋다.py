import sys

N = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

count = 0
for idx in range(N):
    target = nums[idx]
    start = 0
    end = N - 1

    while start < end:
        if start == idx:
            start += 1
            continue
        elif end == idx:
            end -= 1
            continue

        current = nums[start] + nums[end]

        if target == current:
            count += 1
            break
        elif target < current:
            end -= 1
        else:
            start += 1

print(count)
