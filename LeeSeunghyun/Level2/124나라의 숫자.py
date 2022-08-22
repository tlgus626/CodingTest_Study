def solution(n):
    x=n-1 #찾은 규칙에 따라
    answer=''
    while True: #3진법에서 모티브.
        x,y=divmod(x,3) # 몫과 나머지 반환.
        if y==0:
            answer+='1'
        elif y==1:
            answer+='2'
        else:
            answer+='4'
        if x==0:#이게 loop 탈출의 결정적 기준.
            break
        x=x-1
    return answer[::-1] #나머지에 따라 저장된 값을 역순으로 출력 : 진법변환처럼
