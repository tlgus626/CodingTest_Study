def solution(n, k):
    a=""
    #k진수로 변환 
    while n >0 :
        n,mod=divmod(n,k)
        a += str(mod)
    a=a[::-1] 
    
    a=a.split("0")
    if len(a)==0 :
        return 0
    count=0
    
    for i in a:
        if i== "":
            continue
        elif int(i)<2:
            continue
        b=True
        
        # 소수찾기
        for j in range(2,int(int(i)**0.5)+1): 
            if int(i)%j==0:
                b=False
                break
        if b:
            count+=1
                
    return count


    
