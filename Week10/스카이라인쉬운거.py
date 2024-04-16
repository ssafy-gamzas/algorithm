import sys
from collections import deque
input=sys.stdin.readline
stack=deque()
ans=0
for _ in range(int(input())):
  _,y=map(int,input().split())
  if y==0:
    stack.clear()
  elif not stack or stack[-1]<y:
    stack.append(y)
    ans+=1
  else:
    k=stack.pop()
    if stack and stack[-1]==y:
      continue
    while stack and stack[-1]>=y:
      k=stack.pop()
      if k==y:
        stack.append(y)
        break
    else:
      stack.append(y)
      ans+=1
print(ans)
