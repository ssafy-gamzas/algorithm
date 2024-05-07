n,s=map(int,input().split())
li=list(map(int,input().split()))
i,j=0,0
ans,sum=n+1,li[j]
while i<=j:
  if sum>=s: #조건 만족
    num=j-i+1
    if num<ans: # 최소이면 저장
      ans=num
    i+=1 #다음거는 함 빼보자
    sum-=li[i-1]
  elif j<n-1:
    j+=1
    sum+=li[j]
  else:
    break
print(ans if ans<=n else 0)
