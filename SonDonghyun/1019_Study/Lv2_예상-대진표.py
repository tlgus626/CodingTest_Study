def solution(n, a, b):

    cnt = 0
    a, b = a - 1, b - 1

    while a != b:
        a //= 2
        b //= 2
        cnt += 1
        
    return cnt