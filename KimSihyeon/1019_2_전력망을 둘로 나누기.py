cnt = 1


def DFS(graph, visited, node):
    global cnt
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            cnt += 1
            DFS(graph, visited, next_node)


def solution(n, wires):
    global cnt
    answer = float('inf')
    for w in wires:
        tmp = wires[:]
        tmp.remove(w)
        graph = [[] for _ in range(n + 1)]
        for a, b in tmp:
            graph[a].append(b)  # ath node에 연결된 bth node
            graph[b].append(a)
        visited = [False] * (n + 1)
        network = []
        for node in range(1, n + 1):
            if not visited[node]:
                visited[node] = True
                cnt = 1
                DFS(graph, visited, node)
                network.append(cnt)
        answer = min(answer, abs(network[0] - network[1]))
    return answer
