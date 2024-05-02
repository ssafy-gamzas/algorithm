from collections import deque
n,k=map(int,input().split())
ham=deque()
man=deque()
for i,e in enumerate(input()):
  if e=="H":
    ham.append(i)
  else:
    man.append(i)

ans=0
while ham and man:
  a,b=ham.popleft(),man.popleft()
  if abs(a-b)<=k:
    ans+=1
    continue
  if not ham or not man:
    while ham:
      x=ham.popleft()
      if abs(x-b)<=k:
        ans+=1
        break
    while man:
      x=man.popleft()
      if abs(x-a)<=k:
        ans+=1
        break
  elif ham[0]<man[0]:
    man.appendleft(b)
  else:
    ham.appendleft(a)
print(ans)
