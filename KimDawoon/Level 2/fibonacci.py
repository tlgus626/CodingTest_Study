def solution(n):
    
    # 초기값 지정
    a = [0,1]
    
    # 앞의 두 수를 더하고 이를 리스트에 추가
    for i in range(2,n+1):
        a += [a[i-1]+a[i-2]]
    
    # 문제에 제시된 나머지를 구할것
    return a[-1] % 1234567
