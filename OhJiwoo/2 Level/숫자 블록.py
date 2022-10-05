def solution(begin, end):
    answer=[]
    for i in range(begin,end+1):
        a=1
        for j in range(2,int(i**0.5)+1):
            if i % j==0 and i //j < 10000000 :
                a=i//j
                break
        answer.append(a)
    if begin==1 :
        answer[0]=0
    return answer
