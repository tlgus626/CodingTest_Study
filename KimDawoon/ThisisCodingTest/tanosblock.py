# import packages
from collections import deque
import copy as cp

# read data
n, m = map(int, input().split())
maps = []
block = []
for i in range(n):
    road = list(map(int, input()))
    maps.append(road)
    for j in range(m):
        if road[j] == 1:
            block.append([i, j])

# up, down, left, right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# define wall
mincnt = n * m
wall = deque(block)
while wall:
    reject = wall.popleft()
    tmp = cp.deepcopy(maps)
    tmp[reject[0]][reject[1]] = 0
    Q = deque([[0, 0]])
    tmp[0][0] = 1
    cnt = 0
    while Q:
        t = Q.popleft()
        for k in range(4):
            x = t[0] + dx[k]
            y = t[1] + dy[k]
            if 0 <= x < n and 0 <= y < m:
                if tmp[x][y] == 0:
                    Q.append([x, y])
                    tmp[x][y] = tmp[t[0]][t[1]] + 1

    if tmp[n-1][m-1] == 0:
        continue
    else:
        cnt = tmp[n-1][m-1]
        if cnt < mincnt:
            mincnt = cnt

if mincnt == n * m:
    print(-1)
else:
    print(mincnt)

    
#########################################################
# 모범답안 #
# 벽을 하나 부쉴 수 있다는 점
# 불가능이면 -1
# 최단거리 = bfs
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().strip())))
# print("bfs 적용 전",visit)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1  # 벽을 한번 부술 수 있는 상태 에서 시작

    while queue:
        x, y, w = queue.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == 1 and w == 1: # 벽을 만나고 벽을 한번 부술 수 있는 경우
                    visit[xx][yy][0] = visit[x][y][w] + 1
                    queue.append([xx, yy, 0])
                elif graph[xx][yy] == 0 and visit[xx][yy][w] == 0: # 벽이 없고 방문한 적이 없는 경우
                    visit[xx][yy][w] = visit[x][y][w] + 1
                    queue.append([xx, yy, w])
    return -1

print(bfs())
# print("bfs 적용 후", visit)
