from collections import deque

n=int(input())

data=[]
for _ in range(n):
  data.append(list(input()))


dx=[0,0,1,-1]
dy=[1,-1,0,0]

v=[]

def bfs(x,y):
  q=deque()
  q.append((x,y))
  count=1

  while q:
    x,y=q.popleft()
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]

      if 0 <= nx < n and 0 <= ny < n :
        if data[nx][ny] == "1" :
          q.append((nx,ny))
          data[nx][ny]="0"
          count +=1
  v.append(count)
    

for i in range(n) :
  for j in range(n):
    if data[i][j]=="1" :
      data[i][j]="0"
      bfs(i,j)

v.sort()
print(len(v))
for i in range(len(v)):
    print(v[i])
