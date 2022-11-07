def solution(s):
    answer=[0,0]
    while int(s) >1 :
        s_1=0
        for i in range(len(s)):
            if s[i] == '1' :
                s_1 +=1
        answer[0] += 1
        answer[1] += len(s)-s_1
        s=bin(s_1)[2:]
    return answer
