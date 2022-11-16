# 입력
N, M = map(int, input().split())
temp = [[0] * M for _ in range(N)]

block = []
for _ in range(N):
    block.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M: # 맵의 범위 안에 있고
            if temp[nx][ny] == 0: # 0인 부분이면 바이러스가 퍼져서 2가 되도록 하고 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    
    return score

MAX = 0
def make_fence(fence):

    global MAX

    # 울타리 3개 설치가 된 경우
    if fence == 3:

        for i in range(N):
            for j in range(M):
                temp[i][j] = block[i][j]
        
        # 울타리 설치가 반영된 temp 리스트에서 반복 돌려서 2인 부분을 만나면 바이러스 퍼뜨림
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        
        MAX = max(MAX, get_score())
        return
    
    # 울타리 설치를 위한 재귀
    for i in range(N):
        for j in range(M):
            if block[i][j] == 0: # 빈 공간 찾으면 울타리 하나
                block[i][j] = 1
                fence += 1
                make_fence(fence) # 재귀로 돌림. 
                #이때 fence == 3이 되는 stop하는 조건 덕에 재귀가 가능한 것

                block[i][j] = 0 # 하나 빼고 다른 좌표에 대해 재귀하려고
                fence -= 1
