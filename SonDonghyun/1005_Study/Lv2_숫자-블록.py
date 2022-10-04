def yaksu_max(n):
    if n == 1: return 0
    y_max = 1
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            y_max = max(y_max, n // i)

            if y_max > 10000000:
                y_max = 1
            else:
                break
    return y_max

def solution(begin, end):
    return [yaksu_max(i) for i in range(begin, end + 1)]