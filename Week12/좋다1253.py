one={}
input()
li=list(map(int,input().split()))
for x in li:
  if x not in one:
    one[x]=1
  else:
    one[x]+=1

li.sort(reverse=True)
n=len(li)
ans=0
for i in range(n):
  for j in range(n):
    if i==j:
      continue
    k=li[i]-li[j]
    if k==li[j]:
      if li[i]==li[j]:
        if one[k]>2:
          ans+=1
          break
      elif one[k]>1:
        ans+=1
        break
    elif k==li[i]:
      if one[k]>1:
        ans+=1
        break    
    elif k in one:
      ans+=1
      break
print(ans)
