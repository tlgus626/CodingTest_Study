def solution(N, stages):
    
    level = list(range(0,N+1))
    stages.sort()
    
    # stage별 사람들의 실패 인원
    stay = list(map(lambda x: stages.count(x), level))
    
    # 스테이지에 도달한 총 인원을 구함
    # 추후 0으로 나눠지는 것을 방지하기 위해 epsilon값을 대입
    cum = list(map(lambda x: len(stages)+0.0000000001 - sum(stay[0:x]), level))
    
    # 각 구간마다 확률을 구함
    prop = list(map(lambda x, y:x / y, stay, cum))[1:]
    
    # 각 구간별 확률을 구하고 순서대로 배열
    ans = sorted(list(zip(range(1,N+1),prop)),key=lambda x: x[1],reverse=True)
    
    # 순서만 빼와서 리스트로 출력
    return list(list(zip(*ans))[0])
