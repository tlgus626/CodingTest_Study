def solution(progresses, speeds):
    
    # 잡이 0개
    if len(progresses) == 0:
        return []
    
    # 잡이 1개
    elif len(progresses) == 1:
        return [1]
    
    # 잡이 2개 이상
    else:
        # 각 작업이 완료되는 시간 생성
        k = list(map(lambda x, y: (100-x) // y + 1 if (100-x) % y != 0 else (100-x) // y, progresses, speeds))

        a = []
        t = 0
        cnt = 0
        # 왼쪽 값이 오른쪽보다 작을때 까지 count
        for i in k:
            if i > t:
                t = i
                a += [cnt]
                cnt = 1
            else:
                cnt += 1
        a += [cnt]
    return a[1:]
