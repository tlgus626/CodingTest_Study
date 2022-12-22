from collections import deque

M, N, H = map(int, input().split())
graph = []
for _ in range(H):
    g = []
    for _ in range(N):
        l = list(map(int, input().split()))
        g.append(l)
    graph.append(g)

#### setting ####
visit = [[[0] * M for _ in range(N)] for _ in range(H)]
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
dq = deque()

#### initialize ####
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                dq.append((i, j, k, 0))
                visit[i][j][k] = 1

#### BFS ####
while dq:
    nowi, nowj, nowk, days = dq.popleft()
    for l in range(6):
        newi = nowi + dz[l]
        newj = nowj + dx[l]
        newk = nowk + dy[l]
        if 0 <= newi < H and 0 <= newj < N and 0 <= newk < M and visit[newi][newj][newk] == 0 and graph[newi][newj][
            newk] == 0:
            graph[newi][newj][newk] = 1
            visit[newi][newj][newk] = 1
            dq.append((newi, newj, newk, days + 1))

#### output ####
all = True
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                all = False
if all:
    print(days)
else:
    print(-1)
