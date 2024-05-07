import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  n,k,t,m=map(int,input().split())
  score={x:[0]*(k+2) for x in range(1,n+1)}
  for i in range(m):
    id,j,s=map(int,input().split())
    if s>score[id][j]:
      score[id][j]=s
    score[id][0]+=1
    score[id][k+1]=i

  rank=1
  for x in sorted(score.keys(),key=lambda x:(-sum(score[x][1:k+1]),score[x][0],score[x][k+1])):
    if x==t:
      print(rank)
      break
    rank+=1
