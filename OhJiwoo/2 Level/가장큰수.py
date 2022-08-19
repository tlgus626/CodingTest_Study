def solution(numbers):
    a=[]
    #numbers를 문자열로 변환
    for i in numbers:
        a.append(str(i))
    #문자열의 길이를 맞춰서 sort를 실행
    a.sort(key=lambda x: x*3,reverse=True)    
    return str(int(''.join(a)))
