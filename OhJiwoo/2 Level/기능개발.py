from collections import deque
import math
def solution(progresses, speeds):
    answer=[]
    p=[]
    q=deque()
    #각 작업이 걸리는 시간을 구함 
    for i in range(len(progresses)) :
            p=math.ceil((100-progresses[i])/speeds[i])
            q.append(p)
    a=q[0]
    count=0
    #시간 별로 배포 
    while q:
        qq=q.popleft()
        if a >= qq:
            count +=1
        else: 
            answer.append(count)
            a=max(a,qq)
            count=1
    answer.append(count)             
    return answer
