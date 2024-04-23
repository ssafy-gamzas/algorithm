n,x=map(int,input().split())
s=0
ans=[0,0]
tot=0
li=list(map(int,input().split()))
for i,e in enumerate(li):
  if i<x:
    tot+=e
  else:
    if tot>ans[0]:
      ans=[tot,1]
    elif tot==ans[0]:
      ans[1]+=1
    tot=tot+e-li[i-x]

if tot>ans[0]:
  ans=[tot,1]
elif tot==ans[0]:
  ans[1]+=1

if ans[0]==0:
  print("SAD")
else:
  print(ans[0])
  print(ans[1])
  