def solution(name):
    answer = 0
    min_a=0
    min_c=len(name)-1
    #알파벳 횟수 
    for i ,j in enumerate(name):
        min_a+=min(ord(j)-ord('A'), ord('Z')-ord(j)+1) 
        b = i+1
        #'A'가 연속으로 나오는 구간을 찾아서 횟수 비교 
        while b<len(name) and name[b]=='A':
            b +=1
        min_c=min(min_c,2*i+len(name)-b,i+2*(len(name)-b))
    answer = min_a+min_c
    return answer
