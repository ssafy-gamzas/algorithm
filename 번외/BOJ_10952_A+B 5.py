import sys
input = sys.stdin.readline

while 1:
    try:
        print(ord(input().rstrip()))
        A, B = map(int, input().split())
        print(A+B)
    except Exception:
        exit()
