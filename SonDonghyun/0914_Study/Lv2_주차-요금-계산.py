def solution(fees, records):
    from collections import defaultdict

    a = defaultdict(list) # 딕셔너리의 value로 list 받음
    for i in records: # 각 차 번호의 입차 시간을 value값에 append
        a[i[6:10]].append(int(i[0:2]) * 60 + int(i[3:6]))

    for value in a.values():
        if len(value) % 2 != 0: # value중 마지막 출차기록 없는 경우
            value.append(60 * 23 + 59) # 딕셔너리의 value에 23:59 append

    new_dict = defaultdict(int) # 각 차 번호의 총 주차시간 계산
    for key, value in a.items():
        for i, v in enumerate(value):
            if i % 2 == 1:
                new_dict[key] += value[i] - value[i - 1]

    result = []
    for car in sorted(new_dict.keys()): # 주차시간에 따른 요금 계산
        
        if new_dict[car] <= fees[0]: # 기본요금 확인
            result.append(fees[1])
        
        else:
            v = (new_dict[car] - fees[0]) / fees[2]

            if v - int(v) != 0: # 올림 여부 확인
                result.append(fees[1] + (int(v) + 1) * fees[3])
                
            else:
                result.append(fees[1] + int(v) * fees[3])
    
    return result