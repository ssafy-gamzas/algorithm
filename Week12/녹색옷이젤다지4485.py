import sys
from queue import PriorityQueue

input = sys.stdin.readline
tc = 1
while 1:
  n = int(input())
  if n == 0:
    break
  arr = []
  for _ in range(n):
    arr.append(list(map(int, input().split())))
  dist = [[99999999] * n for _ in range(n)]
  q = PriorityQueue()
  dist[0][0] = arr[0][0]
  q.put([arr[0][0], 0, 0])
  dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
  while q:
    d, x, y = q.get()
    if x == n - 1 and y == n - 1:
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        nd = dist[x][y] + arr[nx][ny]
        if nd < dist[nx][ny]:
          q.put([nd, nx, ny])
          dist[nx][ny] = nd
  print(f"Problem {tc}: {dist[n - 1][n - 1]}")
  tc += 1
