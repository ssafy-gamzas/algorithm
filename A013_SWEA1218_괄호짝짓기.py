from collections import deque

def check():
    d = dict()
    for i in range(N):
        if arr[i] == '(':
            if not d.get(arr[i]):
                d[arr[i]] = 0
            d[arr[i]] += 1
        elif arr[i] == '[':
            if not d.get(arr[i]):
                d[arr[i]] = 0
            d[arr[i]] += 1
        elif arr[i] == '{':
            if not d.get(arr[i]):
                d[arr[i]] = 0
            d[arr[i]] += 1
        elif arr[i] == '<':
            if not d.get(arr[i]):
                d[arr[i]] = 0
            d[arr[i]] += 1

        elif arr[i] == ')':
            if not d.get('(') or d.get('(') == 0:
                print("#{} {}".format(t, 0))
                return
            else:
                d['('] -= 1
        elif arr[i] == '}':
            if not d.get('{') or d.get('{') == 0:
                print("#{} {}".format(t, 0))
                return
            else:
                d['{'] -= 1
        elif arr[i] == ']':
            if not d.get('[') or d.get('[') == 0:
                print("#{} {}".format(t, 0))
                return
            else:
                d['['] -= 1
        elif arr[i] == '>':
            if not d.get('<') or d.get('<') == 0:
                print("#{} {}".format(t, 0))
                return
            else:
                d['<'] -= 1

    for k in d.keys():
        if d.get(k) != 0:
            print("#{} {}".format(t, 0))
            return
    print("#{} {}".format(t, 1))


for t in range(1, 11):
    N = int(input())
    arr = list(input())
    if N%2 != 0:
        print("#{} {}".format(t, 0))
        continue
    check()


