nums = [
    "1110111", "0010010", "1011101", "1011011", "0111010", "1101011",
    "1101111", "1010010", "1111111", "1111011"
]
flip = [[0] * 10 for _ in range(10)]
dic = {}
for i in range(10):
  for j in range(i + 1, 10):
    s = 0
    for k in range(7):
      if nums[i][k] != nums[j][k]:
        s += 1
    flip[i][j] = s
    flip[j][i] = s
    if s not in dic:
      dic[s] = {}
    if i not in dic[s]:
      dic[s][i]=[]
    dic[s][i].append(j)
    if j not in dic[s]:
      dic[s][j]=[]
    dic[s][j].append(i)
# print(flip)
print(dic)

N, K, P, X = map(int, input().split())
# 1<=X<=N
# K자리
# 최대 P개

cur = []
tmp = X
zflip = 0
for _ in range(K):
  cur.append(tmp % 10)
  zflip += flip[0][cur[-1]]
  tmp //= 10
print(cur)

# 몇 개 뒤집을건지...
# 가장 끝 자리수면!! N보다 작은지 확인 들어가야한다!!
# 일의 자리부터 충분히 바꿔보자...!

T = len(str(N))


def f(fnum, i):
  if i == T - 1:  #주의
    cs = 1 if fnum > 0 else 0
    for k in dic:
      if cur[i] in dic[k] and fnum + k <= P:
        for x in dic[k][cur[i]]:
          if x < cur[i]:
            cs += 1
    print(fnum,cs)
    return cs
  tmp = f(fnum, i + 1)

  for k in dic:
    if cur[i] in dic[k] and fnum + k <= P:
      tmp += f(fnum + k, i + 1) * len(dic[k][cur[i]])
  return tmp
ans=0
for k in dic:
  if cur[0] in dic[k] and k<= P:
    for x in dic[k][cur[0]]:
      if 0<x<=N:
        ans+=1
if T>1:
  ans//=2
  ans+=f(0,0)
  ans-= 1 if zflip <= P else 0
print(ans)
