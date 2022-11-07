def myftn(x):
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0 and x // y < 10000000:
            return x // y
    else:
        return 1


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            answer.append(myftn(i))
    return answer
