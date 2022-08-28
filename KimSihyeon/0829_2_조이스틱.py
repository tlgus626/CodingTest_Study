def solution(name):
    answer = 0
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # up and down
    for n in name:
        answer += min(alpha.index(n), abs(alpha.index(n) - len(alpha)))
    # left and right
    elem = [i for i, n in enumerate(name) if i == 0 or n != 'A']
    graph = [[0] * len(elem) for _ in range(len(elem))]
    for i in range(len(elem)):
        for j in range(len(elem)):
            ## minimum distance btw elem[i] and elem[j]
            graph[i][j] = graph[j][i] = min(abs(elem[i] - elem[j]),
                                            abs(elem[i] - elem[j] + len(name)),
                                            abs(elem[i] - elem[j] - len(name)))
    # DFS
    check = [0] * len(elem)
    MIN = float('inf')

    def DFS(L, I, S):
        nonlocal MIN
        if S > MIN :
            return
        if L == len(elem):
            if S < MIN:
                MIN = S
                return
        else:
            for i in range(len(elem)):
                if check[i] == 0:
                    check[i] = 1
                    DFS(L + 1, i, S + graph[I][i])
                    check[i] = 0

    DFS(0, 0, 0)
    return answer + MIN
