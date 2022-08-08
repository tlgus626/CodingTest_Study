def solution(n, lost, reserve):
    
    # 두 집단 각각의 차집합
    no = set(lost) - set(reserve)
    yes = set(reserve) - set(lost)
    
    # 여벌이 존재하는 사람: 1, 존재하지 않는 사람: 0
    restrev = list(map(lambda x: 1 if x in yes else 0, list(range(0,n+2))))
    
    # 대여 가능한 사람 배제
    def cnt(restrev,lst):
        cntr = 0
        for i in lst:
            # 자신의 왼쪽 사람이 존재하면 대여
            if restrev[i-1] == 1:
                restrev[i-1] = 0
            
            # 자신의 오른쪽 사람이 존재하면 대여
            elif restrev[i+1] == 1:
                restrev[i+1] = 0
            
            # 대여하지 못한 사람 카운트
            else:
                cntr+=1
        
        # 최종적으로 대여하지 못한 사람을 카운트
        return cntr
    
    return n - cnt(restrev,no)
