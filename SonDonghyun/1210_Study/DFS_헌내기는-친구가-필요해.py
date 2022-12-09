### 최종
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이를 늘려서 해결하기..

n, m = list(map(int, input().split()))

campus = []
for _ in range(n):
    temp = str(input())
    c = [s for s in temp]
    campus.append(c)

start_x, start_y = [(i, j) for i in range(n) for j in range(m) if campus[i][j] == 'I'][0]

visit_str = ['I', 'P', 'O']
visited = [[0] * m for _ in range(n)]

cnt = 0

def dfs(x, y):

    global cnt

    if x <= -1 or x >= n or y <= -1 or y >= m: # n x m 범위를 벗어나거나 벽을 만나면 즉시 종료
        return False

    if campus[x][y] == 'X':
        return False

    if visited[x][y] == 0:
        if campus[x][y] in visit_str:
            visited[x][y] = 1 # 방문처리
            if campus[x][y] == 'P':
                cnt += 1

            # 후 퍼져나감
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            
        return True

    return False

dfs(start_x, start_y)
print([cnt if cnt != 0 else 'TT'][0])