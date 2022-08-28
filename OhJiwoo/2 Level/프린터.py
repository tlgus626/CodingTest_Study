from collections import deque
def solution(priorities, location):
    a=[x for x in range(len(priorities))]
    q=deque(priorities)
    q_a=deque(a)
    answer=0
    while q :
        qq=q.popleft()
        if q:
            if qq< max(q):
                q_a.append(q_a.popleft())
                q.append(qq)
            else:
                answer +=1
                if q_a[0]==location :
                    return answer 
                else: 
                    q_a.popleft()
    return answer +1 
