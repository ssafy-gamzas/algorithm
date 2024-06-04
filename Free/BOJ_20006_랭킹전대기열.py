from collections import defaultdict
import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room = defaultdict(list)

for _ in range(p):
    l, n = input().split()
    l = int(l)

    flag = False
    for key in room.keys():
        level = key[0]
        if abs(l-level) <= 10 and len(room[key]) < m:
            room[key].append([l, n])
            flag = True
            break

    if not flag:
        room[(l, n)].append([l, n])

for key in room.keys():
    room[key].sort(key=lambda x: x[1])
    if len(room[key]) == m:
        print("Started!")
        for value in room[key]:
            print(*value)
    else:
        print("Waiting!")
        for value in room[key]:
            print(*value)


