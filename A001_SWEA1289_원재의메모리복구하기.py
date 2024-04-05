T = int(input())

for t in range(1, T+1):
    value = input()
    ans = 0
    flag = 0

    for i in range(len(value)):
        if value[i] == '1':
            if not flag:
                ans += 1
                flag = 1
        else:
            if flag:
                ans += 1
                flag = 0

    print("#{} {}".format(t, ans))