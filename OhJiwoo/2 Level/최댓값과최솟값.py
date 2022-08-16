def solution(s):
    c=s.split()
    a=[]
    #int 형태로 하나씩 뽑음 
    for i in range(len(c)):
        a.append(int(c[i]))
    #정렬 후 최솟값과 최댓값 출력
    a.sort()
    answer=[]
    answer.append(str(a[0]))
    answer.append(str(a[-1]))
    return " ".join(answer)
