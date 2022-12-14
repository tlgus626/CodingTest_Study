from collections import deque

N = int(input())
graph = []
for _ in range(N) :
    g = list(input())
    g = [int(x) for x in g]
    graph.append(g)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
houses = []

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            dq = deque()
            dq.append((i,j))
            no_house = 1
            graph[i][j] = 0
            while dq :
                nowx, nowy = dq.popleft()
                for k in range(4) :
                    newx = nowx + dx[k]
                    newy = nowy + dy[k]
                    if 0 <= newx < N and 0 <= newy < N and graph[newx][newy] == 1 :
                        dq.append((newx, newy))
                        no_house += 1
                        graph[newx][newy] = 0
            cnt += 1
            houses.append(no_house)

print(cnt)
houses.sort()
for h in houses :
    print(h)
