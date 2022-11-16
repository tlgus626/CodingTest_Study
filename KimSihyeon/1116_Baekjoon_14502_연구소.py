from collections import deque

N, M = 8, 8
graph = [
[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

def get_score(array) :
    score = 0
    for i in range(N) :
        for j in range(M) :
            if array[i][j] == 0 :
                score += 1
    return score

MAX = 0

def make_fence(count) :
    global MAX
    if count == 3 :
        # temporary array
        temp = [[0]*M for _ in range(N)]
        for i in range(N) :
            for j in range(M) :
                temp[i][j] = graph[i][j]
        # virus propagation
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        for i in range(N) :
            for j in range(M) :
                if temp[i][j] == 2 :
                    dq = deque()
                    dq.append((i,j))
                    while dq :
                        nowx, nowy = dq.popleft()
                        for k in range(4) :
                            newx = nowx + dx[k]
                            newy = nowy + dy[k]
                            if 0 <= newx < N and 0 <= newy < M and temp[newx][newy] == 0 :
                                temp[newx][newy] = 2
                                dq.append((newx, newy))
        # safety area
        S = get_score(temp)
        if S > MAX :
            MAX = S
            return
    else :
        # choose walls
        for i in range(N) :
            for j in range(M) :
                if graph[i][j] == 0 :
                    graph[i][j] = 1
                    make_fence(count+1)
                    graph[i][j] = 0

make_fence(0)
print(MAX)
