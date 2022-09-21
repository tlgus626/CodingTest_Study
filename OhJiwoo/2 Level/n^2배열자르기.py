def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        #위치 구하기 
        a = i//n 
        b = i%n  
        if a<b: a,b =b,a  #max(a,b)+1
        answer.append(a+1)
    
    return answer
