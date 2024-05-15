import sys
from collections import deque
input=sys.stdin.readline

r,c=map(int,input().split())
maze=[]
q=deque()
fire=deque()
for i in range(r):
  maze.append(list(input().strip()))
  for j,x in enumerate(maze[i]):
    if x=='J':
      q.append([i,j])
    elif x=='F':
      fire.append([i,j])

dx,dy=[0,0,1,-1],[1,-1,0,0]
road={'J','.'}
ans=1
if q[0][0]==0 or q[0][1]==0 or q[0][0]==r-1 or q[0][1]==c-1:
  print(1)
  exit()
while q:
  qsize=len(fire)
  while qsize>0:
    x,y=fire.popleft()
    for i in range(4):
      nx,ny=x+dx[i],y+dy[i]
      if 0<=nx<r and 0<=ny<c and maze[nx][ny] in road:
        maze[nx][ny]='F'
        fire.append([nx,ny])
    qsize-=1
  qsize=len(q)
  while qsize>0:
    x,y=q.popleft()
    for i in range(4):
      nx,ny=x+dx[i],y+dy[i]
      if 0<=nx<r and 0<=ny<c and maze[nx][ny]=='.':
        maze[nx][ny]='J'
        if nx==0 or ny==0 or nx==r-1 or ny==c-1:
          print(ans+1)
          exit()
        q.append([nx,ny])
    qsize-=1
  ans+=1
print("IMPOSSIBLE")
