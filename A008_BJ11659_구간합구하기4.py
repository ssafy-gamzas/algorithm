import sys
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr2 = [0]
arr2.append(arr[0])
for i in range(1, N):
    arr2.append(arr[i]+arr2[len(arr2)-1])

for _ in range(M):
    a, b = tuple(map(int, input().split()))
    print(arr2[b]-arr2[a-1])