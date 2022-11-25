from collections import deque

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    g = list(map(int, input().split()))
    graph.append(g)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = 0
while True:
    visit = [[0] * N for _ in range(N)]
    is_moved = False
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                ##### BFS #####
                dq = deque()
                # initialize
                dq.append((i, j))
                visit[i][j] = 1
                # make union
                union = [(i, j)]
                cnt = graph[i][j]
                # BFS
                while dq:
                    nowx, nowy = dq.popleft()
                    for k in range(4):
                        newx = nowx + dx[k]
                        newy = nowy + dy[k]
                        if 0 <= newx < N and 0 <= newy < N and visit[newx][newy] == 0 and L <= abs(graph[nowx][nowy] - graph[newx][newy]) <= R:
                            visit[newx][newy] = 1
                            dq.append((newx, newy))
                            union.append((newx, newy))
                            cnt += graph[newx][newy]
                ##### move or stop? #####
                n = len(union)
                if n > 1:
                    for x, y in union:
                        graph[x][y] = int(cnt / n)
                    is_moved = True
    if is_moved == False:
        break
    answer += 1

print(answer)
