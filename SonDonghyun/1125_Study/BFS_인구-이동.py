# 답안
from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):

    united = []
    united.append((x, y))
    
    q = deque()
    q.append((x, y)) # 현재 연합 (시작 국가)

    union[x][y] = index # 현재 연합의 번호
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 연합 내 국가의 수

    while q: # q가 빌 때까지
        x, y = q.popleft() # 현재 연합 내 국가의 좌표

        for i in range(4): # dfs로 사방으로 퍼져
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1: # 설정 좌표 내

                if l <= abs(graph[nx][ny] - graph[x][y]) <= r: # 차이가 l, r 사이이면
                    q.append((nx, ny)) # 연합에 해당 나라 좌표 추가
                    union[nx][ny] = index # 같은 연합 번호 부여
                    summary += graph[nx][ny] # 연합의 인구 수도 sum
                    count += 1 # 연합 국가 수도 sum
                    united.append((nx, ny)) # 연합에 추가
    
    # while문 다 돌면 인구 이동 시작
    for i, j in united:
        graph[i][j] = summary // count # 이미 저장해놓은 summary와 count로 평균 계산
    
    return count # 연합 내 국가 수를 return?

total_count = 0

while True:

    union = [[-1] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    
    if index == n * n:
        break

    total_count += 1

print(total_count)