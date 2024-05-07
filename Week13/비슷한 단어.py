import sys
from collections import defaultdict
words = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]

alpha = defaultdict(int)
target = words[0]
for w in target:
    alpha[w] += 1

count = 0

for word in words[1:]:
    if abs(len(word) - len(target)) > 1:
        continue

    alpha_temp = defaultdict(int)
    for w in word:
        alpha_temp[w] += 1
    isTrue = True
    diff = 0
    for char in set(target + word):
        diff += abs(alpha[char] - alpha_temp[char])

    if diff <= 2 and abs(len(word) - len(target)) <= 1:
        isTrue = True
    else:
        isTrue = False

    if isTrue:
        count += 1

print(count)
