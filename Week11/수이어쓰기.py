check=[0]
k=-1
for x in input():
  x=int(x)
  while k>0:
    if x==check[k]:
      k-=1
      print("*",k,end=' ')
      break
    else:
      k-=1
  else:
    for i in range(1,len(check)):
      if check[i]==x:
        k=i-1
        for j in range(i-1,-1,-1):
          if check[j]!=9:
            break
        else:
          continue
        check[0]+=1
        i=0
        while check[i]>9:
          check[i]=0
          if i==len(check)-1:
            check.append(1)
            break
          i+=1
          check[i]+=1
        break
    else:
      if check[0]<x:
        check[0]=x
        k=len(check)-1
      elif len(check)==1:
        check.append(1)
        k=0
        if x==1:
          check[0]=0
        else:
          check[0]=x
      else:
        check[0]=x
        check[1]+=1
        i=1
        while check[i]>9:
          check[i]=0
          i+=1
          if i==len(check):
            check.append(1)
            if x==1:
              check[0]=0
              k=i-1
            break
          check[i]+=1
          if check[i]==x:
            check[0]=0
            k=i-1
        else:
          k=len(check)-1
    #일단 숫자가 늘어날 건데....
    #현재 자리수 중에 겹치는 수가 있는지 확인! 있다면 어쩌면 +1만 해도 될테니까
    #없다면, 현재 숫자가 1의 자리보다 더 크면 그걸로 업데이트
            #같거나 작으면 10의자리 하나 늘리고 1의 자리를 현재수로 업데이트
            #이때 10의 자리에 따라 100의자리 10000의 자리 바뀌는건 잘 해줘야 한다
      
  print(check)

ans=0
for i,x in enumerate(check):
  ans+=x*10**i
print(ans)