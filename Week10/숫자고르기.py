import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
li=[0]
for i in range(n):
  li.append(int(input()))
ans=set()
for i in range(1,n+1):
  if li[i]==i:
    ans.add(i)
    continue
  elif li[i]<i or i in ans: #불가해서 지나침 or 이미 세트인거 확인 완!
    continue
  q=deque([li[i]])
  dic={li[i]:1}
  while q:
    x=li[q.popleft()]
    if x in dic:
      dic[x]+=1
    elif x==i:
      dic[x]=1
    elif x<i:
      break #만들고 있는게 불가하다
    else:
      dic[x]=1
      q.append(x)
  else:
    ans|=dic.keys()
print(len(ans))
for x in sorted(ans):
  print(x)
