def solution(str1, str2):
  #a1,b1에 2개의 문자를 뽑은 값들 추가 
    a=''
    a1=[]
    b=''
    b1=[]
    answer=[]
    for i in range(1,len(str1)) :
        a+=str1[i-1]
        a+=str1[i]
        if a.isalpha():
            a=a.lower()
            a1.append(a)
        a=''
    for j in range(1,len(str2)) :
        b+=str2[j-1]
        b+=str2[j]
        if b.isalpha():
            b=b.lower()
            b1.append(b)
        b='' 
    a_temp1=a1[:]
    a_temp2=a1[:]
    union=a1[:]
    inter=[]
    #a1과 b1이 둘다 공집합일때 answer =1 
    if a1==[] and b1==[]:
        answer=1*65536
    else:
      #교집합 구하기 
        for k in b1:
            if k in a_temp1:
                a_temp1.remove(k)
                inter.append(k) 
       #합집합 구하기  
        for l in b1:
            if l not in a_temp2:
                union.append(l)
            else:
                a_temp2.remove(l)
        #(교집합/합집합)*65536 에서 1로 나눠 몫만 출력하여 정수부분만 출력         
        answer=((len(inter)/len(union))*65536) // 1     
    return answer
