def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(divmod(i, n)) + 1)
    return answer


################### my another solution ###################

def myftn(n, x):
    res = [0] * n
    for j in range(n):
        if j <= x:
            res[j] = x + 1
        else:
            res[j] = res[j - 1] + 1
    return res


def solution(n, left, right):
    sx, sy = divmod(left, n)
    ex, ey = divmod(right, n)
    answer = []
    if sx == ex:
        onerow = myftn(n, sx)
        for i in range(sy, ey + 1):
            answer.append(onerow[i])
    else:
        # start
        start = myftn(n, sx)
        for i in range(sy, n):
            answer.append(start[i])
        # middle
        for i in range(sx + 1, ex):
            answer.extend(myftn(n, i))
        # end
        end = myftn(n, ex)
        for i in range(ey + 1):
            answer.append(end[i])
    return answer
