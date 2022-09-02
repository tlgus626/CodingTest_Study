def solution(priorities, location):

    count=0
    
    while(len(priorities)!=0):
    
        if location==0: #출력 여부를 확인되는 맨 앞순서로 왔을 경우
        
            if priorities[0]<max(priorities):
            #더 중요도가 큰 문서가 있으면
                priorities.append(priorities.pop(0)) #맨뒤로 보냄
                location=len(priorities)-1 #location을 맨끝으로 설정(배열길이-1)
                
            else: ##더 우선순위가 높은 것이 없다면 내꺼가 출력되는 것이므로 return으로 끝냄
            
                return count+1
                
        else:  
        
            if priorities[0]<max(priorities):
            
                priorities.append(priorities.pop(0))
                location-=1 #맨앞 요소가 뒤로 갔기 때문에 location이 1 줄어듦
                
            else: 
            
                priorities.pop(0) #맨앞요소 출력됨
                location-=1 #맨앞 요소가 출력됐기 때문에 location이 1 줄어듦
                count+=1 #(출력번째수 +1)
