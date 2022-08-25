def solution(priorities, location):
    
    # 순서쌍 출력
    a = list(enumerate(priorities))
    
    for cnt in range(1,len(priorities)+1):
        # 길이가 1이면 단독이므로 그냥 출력
        if len(priorities) == 1:
            return 1
        
        # 길이가 1이 아닐경우 진행
        else:
            # 순서와 항목 분리해서 보기
            una = list(zip(*a))

            # 가장 큰 수 찾기
            mx = max(una[1])
            
            # 찾은 부분 인덱스 가져오기
            indx = list(una[1]).index(mx)
            
            # 큐처럼 토막내서 가장 큰 수보다 앞에있는 리스트를 맨 뒤로
            a = a[indx:] + a[0:indx]
            
            # 가장 큰 수 뽑기
            b = a.pop(0)
            
            # 지정한 수 일경우 작동을 멈추고 결과 출력
            if location == b[0]:
                return cnt
