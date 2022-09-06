from collections import deque
def solution(s):
    q=deque(s)
    a=deque()
    while q :
      #i가 "("라면 a에 추가 
        i=q.popleft()
        if i=="(" :
            a.append(i)
        #q가 ")"일때 
        else: 
          #a가 비어있으면 False
            if a==deque() :
                return False 
            #a가 비어있지 않으면 a에서 1개를 제거 
            else: a.popleft()
    if a==deque():
        return True 
    else: return False
