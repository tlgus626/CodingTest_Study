def solution(n, k):

    # k진수로 숫자 바꾸기
    jinsu = lambda n, k: jinsu(n//k,k) + str(n % k) if n//k != 0 else str(n % k)
    
    # 소수인지 아닌지 판단
    sosu = lambda num: not any(num % c == 0 for c in range(2, int(num**0.5)+1)) if num != 1 else False
    
    # 소수는 살아있고, 소수가 아닌 수는 0
    num = list(map(lambda x: int(x) if x != '' and sosu(int(x)) else 0, jinsu(n, k).split('0')))

    return len(num) - num.count(0)
