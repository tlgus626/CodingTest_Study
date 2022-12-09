from collections import deque

n,m=map(int,input().split())

data=[]
for _ in range(n):
  data.append(list(input()))

visited = [[0]*m for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]



def bfs(x,y):
  q=deque()
  visited[x][y]==1
  q.append((x,y))
  count=0

  while q:
    x,y=q.popleft()
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]

      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] ==0 :
        if data[nx][ny] != "X" :
          q.append((nx,ny))
          visited[nx][ny] =1
          if data[nx][ny]== "P" :
            count +=1
  if count !=0 :
    print(count)
  else:
    print('TT')
    

      
for i in range(n) :
  for j in range(m):
    if data[i][j]=="I" :
      bfs(i,j)
