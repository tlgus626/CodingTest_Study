def solution(n, left, right):
    
    # 알고보니 몫과 나머지 중에서 더 큰 값 채택
    # 정답 1
    return list(map(lambda x: max(divmod(x,n))+1 ,list(range(left,right+1))))

    # 정답 2
    return [max(divmod(x,n))+1 for x in list(range(left,right+1))]
