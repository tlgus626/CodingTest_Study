# import packages
from collections import deque

# read data
n, m, h = map(int, input().split())
hexagon = []
square = []
nice = []

# tomato 3-d t[h][m][n]
for k in range(h):
    for i in range(m):
        road = list(map(int, input().split()))
        square.append(road)
        for j in range(n):
            if road[j] == 1:
                nice.append([k, i, j])
    hexagon.append(square)
    square = []

# up, down, left, right, front, back
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

tomato = sum(sum(hexagon, []), [])
if tomato.count(0) == 0:
    print(0)

Q = deque(nice)
while Q:
    t = Q.popleft()
    for k in range(6):
        x = t[0] + dx[k]
        y = t[1] + dy[k]
        z = t[2] + dz[k]
        if 0 <= x < h and 0 <= y < m and 0 <= z < n:
            if hexagon[x][y][z] == 0:
                Q.append([x, y, z])
                hexagon[x][y][z] = hexagon[t[0]][t[1]][t[2]] + 1

final = sum(sum(hexagon, []), [])

if final.count(0) != 0:
    print(-1)
else:
    print(max(final) - 1)
