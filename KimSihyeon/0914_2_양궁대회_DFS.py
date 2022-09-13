# calculate the difference of scores
def get_score(info, score):
    s = 0
    for i in range(11):
        if score[i] == info[i] == 0:
            continue
        if score[i] > info[i]:
            s += 10 - i
        else:
            s -= 10 - i
    return s


def solution(n, info):
    MAX, answer = 0, [0] * 11

    def DFS(I, L, S):
        nonlocal answer, MAX
        if I == -1 and L:
            return
        if L == 0:
            s = get_score(info, S)
            if s > MAX:
                answer = S[:]
                MAX = s
            return
        for i in range(L, -1, -1):
            S[I] = i
            DFS(I - 1, L - i, S)
            S[I] = 0

    DFS(10, n, [0] * 11)

    if MAX == 0:
        return [-1]
    else:
        return answer