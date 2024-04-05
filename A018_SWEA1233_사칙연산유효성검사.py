for t in range(1, 11):
    N = int(input())
    ans = 1
    for _ in range(N):
        node = list(input().split())
        # print(node)
        if (len(node) == 4 and node[1] not in ['+', '-', '*', '/']) or (len(node) < 4 and node[1] in ['+', '-', '*', '/']):
            ans = 0
    print("#{} {}".format(t, ans))