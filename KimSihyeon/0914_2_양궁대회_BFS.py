from collections import deque


def solution(n, info):
    dq = deque([(0, [0] * 11)])
    MAX = 0
    res = []
    # BFS
    while dq:
        i, score = dq.popleft()
        # number of arrows == n
        if sum(score) == n:
            # calculate each score
            apeach, ryan = 0, 0
            for i in range(11):
                if not (info[i] == 0 and score[i] == 0):
                    if info[i] >= score[i]:
                        apeach += (10 - i)
                    else:
                        ryan += (10 - i)
            # if ryan wins, update MAX
            if ryan > apeach and ryan - apeach >= MAX:
                MAX = ryan - apeach
                res.append(score)
        # number of arrows > n
        elif sum(score) > n:
            continue
        # number of arrows < n
        elif i == 10:
            tmp = score.copy()
            tmp[i] = n - sum(tmp)
            dq.append((-1, tmp))
        # shoot
        else:
            # 1 more arrow than apeach
            tmp = score.copy()
            tmp[i] = info[i] + 1
            dq.append((i + 1, tmp))
            # pass
            tmp2 = score.copy()
            tmp2[i] = 0
            dq.append((i + 1, tmp2))
    # optimal 'res'
    if len(res) == 0:
        return [-1]
    else:
        return res[-1]
