from itertools import product
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for i in range(1, N*2):
        if i % 2 != 0:
            arr.append(str(i//2+1))
        else:
            arr.append('')
    for p in product([" ", "+", "-"], repeat=N-1):
        for i in range(N-1):
            arr[i*2+1] = p[i]
        tmp = ''
        sum = 0
        for a in arr:
            if a not in ('+', '-', ' '):
                tmp += a
            elif a == " ":
                continue
            else:
                sum += int(tmp)
                tmp = a
        sum += int(tmp)
        if sum == 0:
            print(''.join(arr))
    print()