# 시간복잡도 줄인 코드

from collections import Counter # 내장 라이브러리인 collections 사용

def solution(N, stages):
    
    # Counter 함수: stages리스트 내 원소의 개수를 전부 카운트 해서 딕셔너리 형으로 저장
    count_dict = Counter(stages)

    # 여기부터는 위의 풀이와 동일한 접근방식
    n = sum(count_dict.values())

    fail_rate = {} # 딕셔너리로 저장할 거라 중괄호 사용
    
    for i in range(1, N + 1): # O(N)
        
        # Count가 없는(n = 0인) 스테이지부터는 실패율 0으로 저장
        if n == 0: fail_rate[i] = 0
        
        else:

            # 만약 해당 스테이지가 count_dict에 저장이 안되어있으면 cnt = 0 입력
            if i not in count_dict: cnt = 0

            # count_dict에 있는 스테이지면 i번째 스테이지 call 해서 cnt라는 값으로 사용
            else: cnt = count_dict[i]

            # cnt를 전체 사람 수로 나눠 실패율 계산
            fail_rate[i] = cnt / n

            # 스테이지 도달했으나 못 푼 사람을 남은 사람 수에서 빼고 저장
            n -= cnt
    
    # fail_rate 딕셔너리의 value값으로 정렬, 그때의 스테이지 출력
    return sorted(fail_rate, key = lambda x: fail_rate[x], reverse = True)