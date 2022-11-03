# 결국 시현이 답 봄
name = 'AABBAAAAABA'

# 이건 그냥 하는데
def make_dist(name):
    ind_node = [i for i, j in enumerate(name) if i == 0 or j != 'A']
    
    graph = []
    for i in range(len(ind_node)):
        dist = []
        for j in range(len(ind_node)):
            if i < j:
                dist.append(min(ind_node[j] - ind_node[i], ind_node[i] + len(name) - ind_node[j]))
            elif i > j:
                dist.append(min(ind_node[i] - ind_node[j], ind_node[j] + len(name) - ind_node[i]))
            else:
                dist.append(0)

        graph.append(dist)

    return graph, ind_node

dist, node = make_dist(name)
check = [0] * len(node)
MIN = 1e8

def DFS(level, start, dist):
    
    # level은 끊어주려고, 넣은듯

    global MIN
    
    # 이 DFS는 거리를 최소화하는 것이 목적 -> 노드를 도는 중간에 측정한 거리가 최솟값보다 크면 break (return).
    if dist > MIN :
        return
    
    # 노드를 다 돌았을 때, 측정한 거리가 함수 밖에 기록된 최솟값보다 작으면 새로 기록
    if level == len(node):

        if dist < MIN:
            MIN = dist
            return
    
    # 노드를 다 돌지 않았다면 다 돌때까지 반복해야됨
    else:

        for i in range(len(node)):

            if check[i] == 0: # 아직 방문 안 한 노드만 방문

                check[i] = 1 # 방문한거로 표시
                DFS(level + 1, i, dist + dist[start][i]) # level + 1 하고, 거리도 더함
                check[i] = 0 # 방문 안 했다고 되돌려놓아야 다음 iter에서 할 수 있어서 그랬구나

DFS(0, 0, 0)
print(MIN)