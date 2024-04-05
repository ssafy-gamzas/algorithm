for t in range(1, 11):
    N = int(input())
    arr = list(input().split())
    C = int(input())
    cmd = list(input().split())

    for i in range(len(cmd)):
        if cmd[i] == 'I':
            start = int(cmd[i+1])
            l = int(cmd[i+2])
            idx = start
            if start >= N:
                i += l+2
                continue
            elif start+l <= N:
                for j in range(i+3, i+3+l):
                    arr.insert(idx, cmd[j])
                    idx += 1
                i += l + 2
            elif start+l > N:
                for j in range(i+3, i+3+N-start):
                    arr.insert(idx, cmd[j])
                    idx += 1
                i += l + 2

    print("#{} ".format(t), end="")
    for i in range(10):
        print(arr[i], end=" ")
    print()