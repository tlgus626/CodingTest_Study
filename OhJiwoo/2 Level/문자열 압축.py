def solution(s):
    result=[]
    #길이가 1이면 return 1
    if len(s)==1 :
        return 1
    for i in range(1,int(len(s)/2)+1):
        answer =''
        count =1
        a=s[:i]
        for j in range(i,len(s)+i,i):
            b=s[j:i+j]
            if a==b :
                count +=1 
            else: 
                if count==1:
                    answer += a
                else: 
                    answer = answer + str(count) + a
                    count=1
                a=b
        result.append(len(answer))
    return min(result)
