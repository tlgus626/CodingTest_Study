def solution(brown, yellow):
    a=brown+yellow 
    for i in range(1,a+1) :
        if a % i==0 :
            b=a // i 
            if yellow== (i-2)*(b-2):
                return [b,i]
