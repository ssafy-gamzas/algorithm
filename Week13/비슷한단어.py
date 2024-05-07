import sys
from copy import deepcopy
input=sys.stdin.readline
n=int(input())
dic={}

for x in input().rstrip():
  if x not in dic:
    dic[x]=0
  dic[x]+=1
totlen=sum(dic.values())
ans=0
for _ in range(1,n):
  word=input().rstrip()
  if abs(totlen-len(word))>1:
    continue

  tmp={}
  for x in word:
    if x not in tmp:
      tmp[x]=0
    tmp[x]+=1

  if len(dic.keys()-tmp.keys())>1:
    continue
  
  for x in dic:
    if x in tmp:
      tmp[x]-=dic[x]
    else:
      tmp[x]=-dic[x]
  k=0  
  for x in tmp:
    if tmp[x]==0:
      continue
    elif abs(tmp[x])>1 or k>1:
      break
    else:
      k+=1
  else:
    ans+=1
    # print(ans,word)
print(ans)
