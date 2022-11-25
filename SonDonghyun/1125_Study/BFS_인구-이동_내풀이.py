n, l, r = list(map(int, input().split()))

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

print(n, l, r)
print(A)

import copy
from collections import deque

# 국경 개방 한 연합의 인구 이동 후 인구 계산
def pop_move(union, pop):
    total_pop = 0
    for r, c in union:
        total_pop += pop[r][c]
    moved_pop = int(total_pop / len(union))
    return moved_pop

# 절댓값으로 국경 간 인구 차이 계산
abs = lambda x: - x if x < 0 else x

# 그래프 방문 여부 확인-> 나중에 for문 안에 넣어서 초기화 시켜줘야함
visit = [[0] * n for _ in range(n)]

# 사방으로 퍼지기 위한 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 국경 개방한 연합 리스트
union = []

# DFS로 연합국 찾기
def make_union(x, y):

    visit[x][y] = 1 # check visited
    union.append([x, y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:

            if visit[nx][ny] == 0:
                pop_diff = abs(A[nx][ny] - A[x][y])

                if l <= pop_diff <= r:
                    make_union(nx, ny)


def new_pop(a, union):
    new_a = copy.deepcopy(a)
    num_after_move = pop_move(union, new_a)
    for r in range(n):
        for c in range(n):
            if [r, c] in union:
                new_a[r][c] = num_after_move
    return new_a


################################################################
# 여기부터 문제였던 것 같음
from collections import deque
result = 0

dq = deque([[i, j] for i in range(n) for j in range(n)])

while dq: # 국경 개방 후보국 큐가 비어버리면 더 이상 인구이동 없으므로 break
    
    dq = deque([[i, j] for i in range(n) for j in range(n)]) # 빈 큐가 아니었으므로 dq를 일단 다시 초기화
    visit = [[0] * n for _ in range(n)] 
    result += 1
    
    # 모든 x, y에 대해 다 훑어보기
    for i in range(n):
        for j in range(n):
            make_union(n, n)
            if len(union) == 1: # dfs돌렸는데도 국경 개방 안 한 나라는 union길이가 1이므로
                dq.remove([i, j]) # 해당 나라인 [i, j]를 dq에서 삭제
            else:
                A = new_pop(A, union)

print(result)