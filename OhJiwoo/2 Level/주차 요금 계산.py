from collections import defaultdict
def solution(fees, records):
    dict={}
    total = defaultdict(int)
    answer=[]
    for record in records :
        time, number, inout = record.split() # 시간, 차량 번호, inout 할당 
        
        # 시를 분으로 
        h, m = time.split(":")
        time = int(h) * 60 + int(m)
       
      #dict에 있으면 시간 계산 , 없으면 dict에 할당 
        if number in dict :
            total[number]+=time-dict[number]
            del dict[number]
       else: dict[number]=time
    
    #out이 없는 경우 계산 
    max_time = (23 * 60) + 59
    for num, t in dict.items():
        total[num] += max_time - t
        
    car=sorted(total.items())  
    
    #주차 요금 계산 
    for i in range(len(car)):
        if car[i][1]<=fees[0]:
            answer.append(fees[1])
        else :
            fee=(car[i][1]-fees[0])
            if fee % fees[2] ==0 :
                answer.append( (fee //fees[2])*fees[3]+fees[1] ) 
            else: answer.append( ((fee//fees[2])+1)*fees[3]+fees[1])
    return answer
