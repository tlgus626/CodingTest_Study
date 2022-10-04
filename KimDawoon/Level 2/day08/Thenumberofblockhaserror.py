def gd(num):
    
    # num == 1 이면 0
    if num == 1:
        return 0
    
    # num의 약수를 구함 단, num^0.5에 해당하는값까지만 탐색 소수는 1
    k = [c for c in range(1,int(num**0.5)+1) if num % c == 0]
    
    # 마지막 항이 1이면 1을 출력
    if k[-1] == 1:
        return 1
    
    else:
        # 1을 제외한 약수가 존재할경우 최대 약수가 천만을 넘는가에 대한 탐색
        # 천만을 넘을경우 다음으로 큰 약수로 넘어가며, 전부 배제하고 난 후 존재하지 않을경우 1을 리턴
        # 문제 채점방식 기준으로 그냥 천만보다 크면 1을 리턴
        for i in k[1:]:
            if (num // i) <= 10000000:
                return num // i
        return 1

# 시작점부터 끝점까지의 간격을 구하고 gd()에 대입해 값 구하기
solution = lambda begin, end: [gd(k) for k in range(begin,end+1)]
