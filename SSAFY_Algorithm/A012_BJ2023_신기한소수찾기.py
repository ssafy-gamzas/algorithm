N = int(input())


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def make(num):
    if len(num) == N:
        if isPrime(int(num)):
            print(num)
        return

    if not isPrime(int(num)):
        return

    for i in range(1, 10):
        make(num + str(i))


arr = [2, 3, 5, 7]

for a in arr:
    num = str(a)
    make(num)

# dp = [0] * 10**N
#
# for i in range(2, 10**N):
#     dp[i] = i
#
# for i in range(2, 10**N):
#     if dp[i] == 0:
#         continue
#
#     for j in range(i*2, 10**N, i):
#         dp[j] = 0
#
#
# for i in range(10**(N-1), 10**N):
#     if dp[i]:
#         flag = True
#         num = str(dp[i])
#         for j in range(1, N):
#             if not dp[int(num[:j])]:
#                 flag = False
#         if flag:
#             print(dp[i])
