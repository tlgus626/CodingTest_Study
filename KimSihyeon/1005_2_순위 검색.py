def solution(info, query):
    # hash
    comb = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    comb[a + b + c + d] = []
    # info
    for i in info:
        a, b, c, d, score = i.split()
        score = int(score)
        for ax in [a, '-']:
            for bx in [b, '-']:
                for cx in [c, '-']:
                    for dx in [d, '-']:
                        comb[ax + bx + cx + dx].append(score)
    # sort for binary search
    for key in comb.keys():
        comb[key] = sorted(comb[key])
    # check conditions
    answer = []
    for i in range(len(query)):
        q, s = query[i].replace(' and ', '').split()
        scores = comb[q]
        s = int(s)
        MIN, MAX = 0, len(scores) - 1
        res = len(scores)
        while MIN <= MAX:
            MED = (MIN + MAX) // 2
            if s <= scores[MED]:
                res = MED
                MAX = MED - 1
            else:
                MIN = MED + 1
        answer.append(len(scores) - res)
    return answer
