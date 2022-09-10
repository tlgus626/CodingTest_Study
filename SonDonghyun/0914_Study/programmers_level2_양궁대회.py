def solution(n, info):

    # 이 함수는 같은 점수 차이로 이긴다면 더 작은 점수가 많은 배열을 return하기 위한 함수
    def lower_score_comp(a, b):
        for i in range(10, -1, -1):
            if a[i] == b[i]: pass
            elif a[i] > b[i]: return a
            elif a[i] < b[i]: return b


    from itertools import combinations_with_replacement # 중복조합 사용
    from collections import Counter

    score = [i for i in range(10, -1, -1)]
    max_diff = 0
    remember = [0] * 11 # return할 배열 초기값

    for i in combinations_with_replacement(score, n): # 모든 조합을 다 확인할 것임
    
        a = Counter(i)
        ryan_info = [0] * 11 # 라이언 점수 초기화

        # 이번 iter에서 만들어진 조합을 라이언 점수 리스트에 기록
        for j in range(11):
            if j in a.keys():
                ryan_info[10 - j] = a[j]
        
        # 점수 계산 시작
        app_score, ryan_score = 0, 0
        for app, ryan in zip(enumerate(info), enumerate(ryan_info)):
            if app[1] == 0 and ryan[1] == 0:
                pass
            else:
                if app[1] >= ryan[1]:
                    app_score += 10 - app[0]
                else:
                    ryan_score += 10 - ryan[0]
                    
        score_diff = max(ryan_score - app_score, 0) # 점수 차 계산

        if max_diff < score_diff: # 새로 계산한 점수차가 더 클 때
            max_diff = score_diff 
            remember = ryan_info # 업데이트
        
        elif max_diff == score_diff: # 새로 계산한 점수차가 여태 계산한 점수차랑 같은 값일 때
            remember = lower_score_comp(remember, ryan_info) # 더 낮은 점수가 많은 배열을 찾는 함수로 찾아서 저장
    
    if max_diff == 0: # 모든 iter가 끝나고도 0점이면
        return [-1] # 라이언은 못 이김

    return remember