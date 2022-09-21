from collections import deque
def solution(prices):
    q=deque(prices) 
    answer = []
    while q :
        a=q.popleft() #1초 시점을 뽑아서 비교 
        count=0
        for i in q :
            count +=1
            if a > i : #떨어지면 break
                break
        answer.append(count)        
    return answer
