def solution(n, lost, reserve):
    for i in range(1,n+1) :
        if i in lost and i in reserve:
            reserve.remove(i) 
            lost.remove(i)
    for j in range(1, n+1):
        if j in lost :
            if (j - 1) in reserve :
                reserve.remove(j - 1)
                lost.remove(j)
            elif (j + 1) in reserve :
                reserve.remove(j + 1)
                lost.remove(j)

    return n - len(lost)
