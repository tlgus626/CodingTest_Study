def solution(n, info):

    def a_or_b(a, b): # 같은 점수 차이로 이긴다면 작은 점수가 많은 배열을 return하기 위한 함수
        for i in range(10, -1, -1):
            if a[i] > b[i]: return a
            elif a[i] < b[i]: return b

    from itertools import combinations_with_replacement # 중복조합 사용
    from collections import Counter

    score = [i for i in range(10, -1, -1)]
    max_diff = 0
    remember = [0] * 11 # return할 배열 초기값

    for i in combinations_with_replacement(score, n): # 모든 조합을 다 확인
        a = Counter(i)
        ryan_info = [a[j] if j in a.keys() else 0 for j in range(11)] # 라이언의 기록

        # 점수 계산 시작    
        apeach_score, ryan_score = 0, 0
        for apeach, ryan in zip(enumerate(info), enumerate(ryan_info)):
            if apeach[1] != 0 or ryan[1] != 0:
                if apeach[1] >= ryan[1]: apeach_score += 10 - apeach[0]
                else: ryan_score += 10 - ryan[0]
                    
        score_diff = max(ryan_score - apeach_score, 0) # 점수 차 계산

        if max_diff < score_diff: # 새로 계산한 점수차가 더 클 때
            max_diff = score_diff
            remember = ryan_info # 업데이트

        elif max_diff == score_diff: # 새로 계산한 점수차이가 최대점수차이랑 같을때
            remember = a_or_b(remember, ryan_info) # 조건에 더 부합하는 배열을 저장
    
    return remember if max_diff != 0 else [-1]