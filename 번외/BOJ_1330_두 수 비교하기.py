"""
if A > B:
    print(">")


"""

# 1 2 <1, 공백, 2> -> 1, 2  (1,2) -> 1과 2가 잇구나!!!!
# def __init__(self, func, *iterables):
#     pass
#
#
A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
elif A == B:
    print("==")


