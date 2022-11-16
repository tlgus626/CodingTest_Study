import itertools
import copy

n,m = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

c = []

for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            c.append([i,j])

wall = list(itertools.combinations(c,3))


def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx>-1 and ny>-1 and nx < n and ny < m :
            if data_1[nx][ny] == 0:
                data_1[nx][ny] = 2
                virus(nx,ny)



def count_safe(now):
    safe_count = 0
    for i in range(n):
        safe_count += now[i].count(0)

    return safe_count


result = 0
for new_wall in wall:
    data_1 = copy.deepcopy(data)
    for new in new_wall :
        data_1[new[0]][new[1]] = 1

    for i in range(n):
        for j in range(m):
            if data_1[i][j] == 2:
                virus(i,j)

    result = max(result,count_safe(data_1))


print(result)
  
