import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
q=deque()
for i in range(n):
  li=list(map(int,input().split()))
  if i==0:
    q.append([li[0],0,0])
    q.append([li[0],0,1])
    for j in range(1,m-1):
      q.append([li[j],j,-1])
      q.append([li[j],j,0])
      q.append([li[j],j,1])
    q.append([li[m-1],m-1,0])
    q.append([li[m-1],m-1,-1])
  elif i==n-1:
    ans=1000
    while q:
      x,c,d=q.popleft()
      s=x+li[c+d]
      if s<ans:
        ans=s
    print(ans)
  else:
    qsize=len(q)
    for _ in range(qsize):
      x,c,d=q.popleft()
      nc=c+d
      s=x+li[nc]
      for k in {-1,0,1}:
        if k==d or nc+k<0 or nc+k>=m:
          continue
        q.append([s,nc,k])
