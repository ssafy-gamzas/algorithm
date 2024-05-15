import sys
input=sys.stdin.readline

n,m=map(int,input().split())
title={}
nums=[]
for _ in range(n):
  t,k=input().split()
  k=int(k)
  if k not in title:
    title[k]=t
    nums.append(k)

def find(x,l,r):
  mid=(l+r)//2
  if x<=nums[mid]:
    if mid>0 and x<=nums[mid-1]:
      return find(x,l,mid-1)
    return mid
  else:
    if mid+1<len(nums) and nums[mid+1]<x:
      return find(x,mid+1,r)
    return mid+1

for _ in range(m):
  x=int(input())
  n=find(x,0,len(nums)-1)
  print(title[nums[n]])
