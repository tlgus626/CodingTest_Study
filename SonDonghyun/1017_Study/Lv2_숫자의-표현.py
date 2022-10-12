def solution(n):
    
    cnt = 0
    for i in range(1, int(n // 2) + 1):
        x = i
        sum = 0

        while sum < n :
            sum += x
            x += 1

        if sum == n:
            cnt += 1

    return cnt + 1