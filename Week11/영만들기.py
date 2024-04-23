import sys
input = sys.stdin.readline
tc = int(input())


def f(idx, n, li):
  if idx == n-1:
    nums = list(range(2, n + 1))
    stack = [1]
    for i, e in enumerate(li):
      if e == ' ':
        stack[-1] = stack[-1] * 10 + nums[i]
      else:
        stack.append(e)
        stack.append(nums[i])
    ans=stack[0]
    for i in range(1,len(stack),2):
      if stack[i] == '+':
        ans+=stack[i+1]
      else:
        ans-=stack[i+1]
    if ans==0:
      for i in range(1,n):
        print(i,end='')
        print(li[i-1],end='')
      print(n)
    return
  
  for x in [' ','+', '-']:
    li[idx]=x
    f(idx+1,n,li)



for tcn in range(tc):
  n = int(input())
  if tcn > 0:
    print()
  f(0,n,[' ']*(n-1))