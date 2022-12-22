from collections import deque 
M, N, H = map(int, input().split())
box= []
queue=deque()
day=0


for _ in range(H) :
  a=[]
  for _ in range(N) :
    a.append(list(map(int,input().split())))
  box.append(a)  
   
    

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]



for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))


while queue :
  x,y,z=queue.popleft()
  for i in range(6) :
    nx= x+dx[i]
    ny= y+dy[i]
    nz= z+dz[i]
    if  0<= nx < H and 0<= ny < N and 0<= nz < M and box[nx][ny][nz] ==0 :
      box[nx][ny][nz] = box[x][y][z] +1
      queue.append([nx,ny,nz])

      
      

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        day = max(day, max(j))
print(day-1)

              
