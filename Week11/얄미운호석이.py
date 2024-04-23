import sys

def format_number(n, l):
    return f'{n:0{l}d}'

def count_diff(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

number_arr = {
    0: '1110111',
    1: '0010010',
    2: '1011101',
    3: '1011011',
    4: '0111010',
    5: '1101011',
    6: '1101111',
    7: '1010010',
    8: '1111111',
    9: '1111011',
}

N, K, P, X = map(int, sys.stdin.readline().split())

X_formatted = format_number(X, K)

answer = 0

for num in range(1, N+1):
    num_formatted = format_number(num, K)
    diff = 0
    for i in range(K):
        diff += count_diff(number_arr[int(X_formatted[i])], number_arr[int(num_formatted[i])])
    if diff <= P and num != X:
        answer += 1

print(answer)
