N, K = map(int, input().split())
arr = list(input())
ans = 0

for i in range(N):
    if arr[i] == 'P':
        for j in range(i-K, i+(K+1)):
            if not (0 <= j < N):
                continue
            if arr[j] == 'H':
                ans += 1
                arr[j] = ' '
                break

print(ans)