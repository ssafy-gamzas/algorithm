S, P = tuple(map(int, input().split()))
DNA = list(input())
limit = list(map(int, input().split()))
arr = [[0, 0, 0, 0]]
ans = 0

for i in range(S):
    tmp = [0, 0, 0, 0]

    if DNA[i] == 'A':
        tmp[0] += 1
    elif DNA[i] == 'C':
        tmp[1] += 1
    elif DNA[i] == 'G':
        tmp[2] += 1
    elif DNA[i] == 'T':
        tmp[3] += 1

    for j in range(4):
        tmp[j] += arr[i][j]
    arr.append(tmp)

for i in range(1, S-P+2):
    cnt = 0
    for j in range(4):
        if limit[j] <= arr[i+P-1][j]-arr[i-1][j]:
            cnt += 1
        else:
            break
    if cnt == 4:
        ans += 1

print(ans)

