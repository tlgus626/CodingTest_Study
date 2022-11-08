from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)

distance = [-1] * N  # minimum distance from `X`

dq = deque()

# initialize
distance[X - 1] = 0
dq.append(X - 1)

# BFS
while dq:
    now = dq.popleft()
    for i in range(N):
        # can visit
        if i in graph[now]:
            # not visited yet
            if distance[i] == -1:
                distance[i] = distance[now] + 1
                dq.append(i)

check = False
for i in range(N):
    if distance[i] == K:
        print(i + 1)
        check = True
if check == False:
    print(-1)

##### dynamic programming ver.

N, M, K, X = map(int, input().split())

graph = [[0]*N for _ in range(N)]
for _ in range(M) :
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

for i in range(N) :
    for j in range(N) :
        for k in range(N) :
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

check = False
for i in range(N) :
    if distance[i] == K :
        print(i+1)
        check = True
if check == False :
    print(-1)