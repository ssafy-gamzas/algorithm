nums = [
    "1110111", "0010010", "1011101", "1011011", "0111010", "1101011",
    "1101111", "1010010", "1111111", "1111011"
]
flip = [[0] * 10 for _ in range(10)]
for i in range(10):
  for j in range(i + 1, 10):
    s = 0
    for k in range(7):
      if nums[i][k] != nums[j][k]:
        s += 1
    flip[i][j] = s
    flip[j][i] = s

N, K, P, X = map(int, input().split())
# 1<=X<=N
# K자리
# 최대 P개

cur = []
tmp = X
for _ in range(K):
  cur.append(tmp % 10)
  tmp //= 10
ans=0
for i in range(1,N+1):
  if i==X:
    continue
  zflip=0
  for j in range(K):
    a=(i//(10**j))%10
    zflip+=flip[cur[j]][a]
    if zflip>P:
      break
  if zflip<=P:
    ans+=1
print(ans)
