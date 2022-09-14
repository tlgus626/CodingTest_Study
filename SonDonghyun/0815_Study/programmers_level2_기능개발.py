from collections import deque # 선입선출을 위해 큐 자료형 사용

def solution(progresses, speeds):

    # 남은 날짜를 계산 (소수점이어도 괜찮음)
    day_left = deque([(100 - i) / j for i, j in zip(progresses, speeds)])

    day = 0
    result = []

    # 큐가 빌 때까지 반복
    while day_left != deque([]):

        # 매 반복마다 날짜 하루씩 추가
        day += 1

        # 현재 날짜보다 큐의 첫번째 인덱스에 적힌 남은 날짜가 더 적으면
        if day_left[0] <= day:
            
            release_cnt = 0 # 그 날 몇 개 기능이 릴리즈 되는지 카운트

            while day_left[0] <= day: # 그 날 릴리즈 되는 모든 기능을 pop할 때까지 반복

                day_left.popleft()
                release_cnt += 1 # 카운트

                if day_left == deque([]): break # 이걸 안 써주면 마지막 릴리즈 카운트를 못 기록함
        
            result.append(release_cnt) # 카운트를 기록

    return result