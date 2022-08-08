def solution(N, stages):

    # 실패율 계산 (분자, 분모 각각 계산)
    nom = [0]*(N+1)
    den = [len(stages)]*(N+1)

    for i in range(len(stages)) :
        if stages[i] <= N :
            nom[stages[i]] += 1
            for j in range(stages[i]+1, N+1) :
                den[j] -= 1
    
    # 스테이지 별 실패율 리스트 생성
    res = []
    for i in range(1, N+1) :
        if nom[i] == 0 and den[i] == 0 :
            fail_ratio = 0
        else :
            fail_ratio = nom[i]/den[i]
        res.append((i, fail_ratio))

    # 실패율 기준 내림차순, 스테이지 기준 오름차순 정렬
    res.sort(key = lambda x : (-x[1], x[0]))

    # 리스트 요소는 (스테이지, 실패율)로 되어있으므로 스테이지만 가져와서 answer 반환
    answer = []
    for r in res :
        answer.append(r[0])

    return answer