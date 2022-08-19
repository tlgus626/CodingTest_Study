def solution(n):

    s = ''

    while n:
        m = n % 3
        n //= 3

        if m == 0:
            s = '4' + s
            n -= 1

        else:
            s = str(m) + s
    
    return s
