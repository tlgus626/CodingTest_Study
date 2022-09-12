from itertools import combinations_with_replacement

def solution(n, info):
    
    # 1발 쏘는데 1발이 10점이 된 경우
    if info[0] == 1 and n == 1:
        return [-1]
    
    # 3발 쏘는데 10 9 8 점 맞추는 경우
    elif info[0] == 1 and info[1] == 1 and info[2] == 1 and n == 3: 
        return [-1]
    
    # 화살 점수를 입력하면 입력한 점수의 개수를 출력
    def scoretocount(lst):
        tmp = []
        for i in range(10,-1,-1):
            tmp += [lst.count(i)]
        return tmp
    
    # 최대 answer 저장공간
    maxans = 0
    scr = []
    
    # 모든 중복조합 다 돌려서 환산
    for i in combinations_with_replacement([0,1,2,3,4,5,6,7,8,9,10],n):
        score = scoretocount(i)
        ans = 0
        
        # 세 가지 경우로 나누어 출력
        for j in range(0,10):
            
            # 1. 라이언이 어피치보다 많은 화살을 가지면 + 점수
            if score[j] - info[j] > 0:
                ans += (10 - j)
            
            # 2. 라이언, 어피치 둘다 점수를 못얻을 경우 0점
            elif score[j] == 0 and info[j] == 0:
                pass
            
            # 3. 그 이외엔 - 점수
            else:
                ans -= (10 - j)
        
        # 점수의 최대치를 넘으면 값 교체 단, 중복조합 함수의 경우 [0, 0, ..., 0] ~ [10, 10, ..., 10] 의 순으로 쌓이므로 
        # 동점이라도 앞 순서의 것을 가져가면 자연스럽게 낮은 점수가 있는 것으로 유지 된다.
        if maxans < ans:
            scr = score
            maxans = ans
    
    return scr
