import sys

N = int(sys.stdin.readline())
cs = [int(sys.stdin.readline()) for _ in range(N)]


def bt(st, i):
    global limit
    if i > limit:
        if eval(st.replace(" ", "")) == 0:
            answer.append(st)
        return
    bt(st + " " + str(i), i + 1)
    bt(st + "-" + str(i), i + 1)
    bt(st + "+" + str(i), i + 1)


for limit in cs:
    answer = []
    bt("1", 2)
    for a in sorted(answer):
        print(a)
    print()
