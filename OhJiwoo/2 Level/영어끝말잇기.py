def solution(n, words):
    count=1
    a=[]
    answer=[]
    for i in range(1,len(words)):
        count +=1 
        a.append(words[i-1])
        if words[i-1][-1] !=words[i][0] or words[i] in a : #마지막과 시작단어가 다르거나 나온 단어면 break
            if count % n ==0 :
                answer.append(n)
                answer.append(count // n)
                break
            else: 
                answer.append(count % n )
                answer.append((count //n) +1)
                break
    if answer==[]:
        answer=[0,0]
    return answer
