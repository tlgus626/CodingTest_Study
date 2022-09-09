def solution(fees, records):
    
    # 시간, 차번호, 입출여부로 각각 나눠서 리스트로 받아들이기 및 차별로 받아드림
    우왕 = sorted(list(map(lambda s: s.split(' '),records)),key=lambda x: x[1] + x[0])
    
    # 차 번호 받아들일 딕셔너리
    ㅋ = {오케이[1]:0 for 오케이 in 우왕}
    for i in 우왕:
        if i[2] == "IN":
            ㅋ[i[1]] = ㅋ[i[1]] - int(i[0][:2]) * 60 - int(i[0][3:])

        elif i[2] == "OUT":
            ㅋ[i[1]] = ㅋ[i[1]] + int(i[0][:2]) * 60 + int(i[0][3:])

    # 주차 했던 시간 출력
    주차시간 = list(map(lambda x: x + 1439 if x <= 0 else x, ㅋ.values()))
    
    # 올림 함수
    ceil = lambda x: x // 1 + 1 if x % 1 != 0 else x
    
    # 차별 주차요금 계산
    return list(map(lambda x: (ceil((x-fees[0])/fees[2]))*fees[3]+fees[1] if x-fees[0] > 0 else fees[1], 주차시간))
