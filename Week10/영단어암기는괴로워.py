import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dic={}
for _ in range(n):
  word=input().rstrip()
  if len(word)<m:
    continue
  if word not in dic:
    dic[word]=1
  else: 
    dic[word]+=1
for word in sorted(dic.keys(), key=lambda x:(-dic[x],-len(x),x)):
  print(word)
