import sys
input=sys.stdin.readline
n=int(input())
money=list(map(int,input().split()))
total=int(input())
if sum(money)<=total:
  print(max(money))
  exit()
money.sort()
l,r=0,n
while l<r:
  mid=(l+r)//2
  x=sum(money[:mid+1])
  num=n-mid-1
  xr=x+money[mid+1]*num
  xl=x+money[mid]*num
  if xl<=total<xr:
    k=(total-xl)//num
    print(money[mid]+k)
    exit()
  elif xl>total:
    r=mid
  else:
    l=mid
print(total//n)
