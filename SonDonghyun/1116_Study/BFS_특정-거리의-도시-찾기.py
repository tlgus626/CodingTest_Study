n, m, k, x = list(map(int, input().split()))

# 방향 표시해주는 direction 리스트
direction = []
for _ in range(m):
    direction.append(list(map(int, input().split())))

def make_graph(direction):
    graph = [[] for _ in range(n + 1)]
    for dir in direction:
        graph[dir[0]].append(dir[1])
    return graph

graph = make_graph(direction)

distance = [-1] * (n + 1)
distance[x] = 0

from collections import deque
q = deque([x])
while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)