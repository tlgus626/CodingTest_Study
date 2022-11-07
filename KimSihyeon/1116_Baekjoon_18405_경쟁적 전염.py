from collections import deque

N, K = map(int, input().split())
graph = []
for _ in range(N):
    g = list(map(int, input().split()))
    graph.append(g)
S, X, Y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dq = []

# where is virus?
for i in range(N):
    for j in range(N):
        v = graph[i][j]
        if v != 0:
            dq.append((v, i, j, 0))  # virus_type, location_x, location_y, seconds

# sort queue
dq = deque(sorted(dq, key=lambda x: x[0]))

# virus propagation
while dq:
    t, nowx, nowy, sec = dq.popleft()
    if sec == S:
        break
    for j in range(4):
        newx = nowx + dx[j]
        newy = nowy + dy[j]
        if 0 <= newx < N and 0 <= newy < N and graph[newx][newy] == 0:
            graph[newx][newy] = t
            dq.append((t, newx, newy, sec + 1))

print(graph[X - 1][Y - 1])
