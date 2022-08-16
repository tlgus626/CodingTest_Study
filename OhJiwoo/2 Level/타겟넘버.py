def solution(numbers, target):
    answer = 0
    a=[0]
    for i in numbers:
        b=[]
    #값을 하나씩 뽑아서 더하고 뺌     
        for j in a:
            b.append(j+i)
            b.append(j-i)
        a=b
    #target과 같은 값을 가진 것만 count    
    for k in b:
        if k == target :
            answer +=1
    return answer
