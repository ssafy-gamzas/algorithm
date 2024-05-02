nums=list(map(int,input()))
n=len(nums)
i=0
for x in range(1,99999999):
  for e in map(int,str(x)):
    if e==nums[i]:
      i+=1
      if i==n:
        print(x)
        exit()
