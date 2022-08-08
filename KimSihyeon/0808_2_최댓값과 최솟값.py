def solution(s):

    # 최솟값과 최댓값 initialize
    MIN = float('inf')
    MAX = -float('inf')

    for n in s.split(' ') :
        n = int(n)
        if MIN > n : MIN = n
        if MAX < n : MAX = n

    return str(MIN) + ' ' + str(MAX)