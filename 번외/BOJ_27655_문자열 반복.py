T = int(input())

for _ in range(T):
    R, S = input().split()
    for s in S:
        for _ in range(int(R)):
            print(s, end="")
    print()