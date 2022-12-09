from collections import deque

# N = 7
N = int(input())

mapd = []
for i in range(N):
    tmp = list(map(int, input().split()))
    mapd.append(tmp)

#mapd = [[0,1,1,0,1,0,0],
#      [0,1,1,0,1,0,1],
#      [1,1,1,0,1,0,1],
#      [0,0,0,0,1,1,1],
#      [0,1,0,0,0,0,0],
#      [0,1,1,1,1,1,0],
#      [0,1,1,1,0,0,0]]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
dab = []
while True:
    hap = sum(sum(mapd,[]))
    if hap == 0:  
        break
      
    i = 0
    j = 0
    a = [N, N]
    for i in range(N):
        j = 0
        for j in range(N):
            if mapd[i][j] == 1:
                a = [i,j]
                break
        if a != [N, N]:  
            break
  
    k = 0
    Q = deque([a])
    cnt = 0
    while Q:
        tmp = Q.popleft()
        for k in range(0,4):
            x = dx[k] + tmp[0]
            y = dy[k] + tmp[1]
            if 0 <= x < N and 0 <= y < N:
                if mapd[x][y] == 1:
                    cnt += 1
                    mapd[x][y] = 0
                    Q.append([x, y])
  
    dab += [cnt]

print(len(dab))
for z in range(len(dab)):
    print(dab[z])
