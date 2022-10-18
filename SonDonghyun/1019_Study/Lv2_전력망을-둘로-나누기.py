### dfs 성공
def make_graph(n, wires):
    graph = [set() for i in range(n + 1)]
    for i in wires:
        graph[i[0]].add(i[1])
        graph[i[1]].add(i[0])
    return [list(i) for i in graph]

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def solution(n, wires):
    abs = lambda x: -x if x < 0 else x
    min_diff = 1e9
    for i in wires:
        a = wires.copy()
        a.remove(i)
        visited = [False] * (n + 1)
        for i in a:
            dfs(make_graph(n, a), a[0][0], visited)
        min_diff = min(min_diff, (abs(sum(visited) - (n - sum(visited)))))

    return min_diff