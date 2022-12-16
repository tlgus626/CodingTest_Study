from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    g = list(input())
    graph.append(g)

visit = [[0] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

cnt = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            dq = deque()
            visit[i][j] = 1
            dq.append((i, j))
            while dq:
                nowx, nowy = dq.popleft()
                for k in range(4):
                    newx = nowx + dx[k]
                    newy = nowy + dy[k]
                    if 0 <= newx < N and 0 <= newy < M and visit[newx][newy] == 0:
                        if graph[newx][newy] == 'O':
                            visit[newx][newy] = 1
                            dq.append((newx, newy))
                        if graph[newx][newy] == 'P':
                            visit[newx][newy] = 1
                            dq.append((newx, newy))
                            cnt += 1

if cnt > 0:
    print(cnt)
else:
    print('TT')
