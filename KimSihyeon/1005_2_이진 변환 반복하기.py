# number of 0s, length after removing 0s
def del0(s):
    cnt = 0
    res = ''
    for x in s:
        if x == '0':
            cnt += 1
        else:
            res += x
    return cnt, len(res)

# from digit to binary number
def get2(s):
    res = ''
    while s > 0:
        res += str(s % 2)
        s //= 2
    return res[::-1]


def solution(s):
    zero_cnt = 0
    transform_cnt = 0
    while True:
        cnt, len = del0(s)
        zero_cnt += cnt
        transform_cnt += 1
        s = get2(len)
        if s == '1':
            break
    return [transform_cnt, zero_cnt]
