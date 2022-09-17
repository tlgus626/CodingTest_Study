from collections import deque
def solution(prices):
    
    empty = []
    
    # 큐로 받아들이자
    Q = deque(prices)
    while Q:
        
        cnt = 0
        num = Q.popleft()
        
        # 맨 앞의 하나를 빼 남은 주식가격과 비교해서 떨어진 지점까지 count
        for a in Q:
            cnt += 1
            if num > a:
                break
        
        # count한 숫자 대입
        empty += [cnt]
    return empty
