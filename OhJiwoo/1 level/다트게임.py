def solution(dartResult):
    n=''
    answer=[]
    for i in dartResult :
      #isnumeric이 true 경우에 입력
      if i.isnumeric():
            n +=i 
      #S,D,T 일때의 경우를 구해서 answer에 추가 
        elif i=='S':
            n= int(n)**1
            answer.append(n)
            n=''      
        elif i=='D':
            n=int(n)**2
            answer.append(n)
            n=''      
        elif i=="T":
            n=int(n)**3
            answer.append(n)
            n=''
       #*인 경우 길이가 1이면 하나의 값만 2배, 2이상이면 2개의 값에 2배     
        elif i=='*':
            if len(answer)==1:
                answer[0]=answer[0]*2
            else: 
                answer[-1]=answer[-1]*2
                answer[-2]=answer[-2]*2
       # #인 경우 마이너스          
        elif i=="#":
            answer[-1]=answer[-1]*(-1)           
    #구한 값을 모두 더해서 출력 
    answer=sum(answer)        
    return answer
