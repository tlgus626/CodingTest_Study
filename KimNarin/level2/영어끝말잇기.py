def solution(n, words):
    answer=[]
    for i,w in enumerate(words):
        if w in words[:i] or (w[0] !=words[i-1][-1] and i!=0):   # 앞뒤 펄자 틀린 것과 반복 리스트 중 어느하나라도 틀리면 개수 카운트
            answer=[i%n+1,i // n +1 ]
            break


    if len(answer)==0:
        answer=[0,0]
            
    
    
    
    return answer
