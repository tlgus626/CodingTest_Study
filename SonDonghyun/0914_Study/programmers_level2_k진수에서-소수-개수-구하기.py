def solution(n, k):
    
    # 소수 판별 함수 정의
    import math
    def is_prime(x):
        if x == 1:
            return False

        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    # k진수 변환, 문자열 형식으로 저장
    a = ''
    while n:
        n, l = divmod(n, k)
        a = str(l) + a

    # 변환한 수에서 소수 판별
    cnt = 0
    while a:

        if '0' in a: 
            if a[0] == '0': a = a[1:]
            else:
                if is_prime(int(a[:a.index('0')])): cnt += 1
                a = a[a.index('0') + 1:]
        else:
            if is_prime(int(a)): cnt += 1
            break
        
    return cnt