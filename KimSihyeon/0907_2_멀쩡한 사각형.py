# 최대공약수 구하는 함수
def myftn(MIN, MAX):
    res = 1
    for i in range(2, MIN + 1):
        if MIN % i == 0 and MAX % i == 0:
            res = i
    return res


def solution(w, h):
    MIN, MAX = min(w, h), max(w, h)
    gcd = myftn(MIN, MAX)
    return MAX * MIN - (MAX + MIN - gcd)
