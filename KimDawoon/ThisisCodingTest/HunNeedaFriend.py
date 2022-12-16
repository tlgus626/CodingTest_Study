# import packages
from collections import deque

# read data
n, m = map(int, input().split())
maps = []
Doyeon = []
visit = []
for i in range(n):
    campus = list(input())
    visit.append([0] * len(campus))
    maps.append(campus)
    for j in range(m):
        if campus[j] == "I":
            Doyeon = [i, j]

# move point
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# define deque
Q = deque([Doyeon])

# count person
cnt = 0

# BFS
while Q:
    place = Q.popleft()
    visit[place[0]][place[1]] = 1
    for k in range(4):
        x = place[0] + dx[k]
        y = place[1] + dy[k]
        if 0 <= x < n and 0 <= y < m:
            if maps[x][y] == "P" and visit[x][y] == 0:
                cnt += 1
                Q.append([x, y])
                visit[x][y] = 1
            elif maps[x][y] == "O" and visit[x][y] == 0:
                Q.append([x, y])
                visit[x][y] = 1

# solution 
if cnt == 0:
    print("TT")
else:
    print(cnt)
