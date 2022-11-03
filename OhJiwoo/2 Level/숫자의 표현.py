def solution(n):
    count=1
    for i in range(1,n//2+1):
        a=0
        while (a<n):
            a +=i
            i += 1
        if a==n :
            count +=1
    return count
