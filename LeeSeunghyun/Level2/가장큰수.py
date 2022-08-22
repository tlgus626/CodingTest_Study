def solution(numbers) :
    
    res = []
    
    for number in numbers: #받은 숫자 리스트들을 다 훑음
        prev = str(number) #원 숫자(원 데이터) 저장하는 변수
        add = list(str(number)) #네 자리수로 변환 된 값을 저장하는 변수

        i = 0
        
        ##아이디어 : 각각의 숫자들을 네 자리로 변환시켜줌
        while len(add) < 4:
            add.append(prev[i])
            i = (i + 1) % len(prev) ##랜덤하게 주어지는 숫자의 자리수에 대응. 나머지 계산
    
        #print(f"중간체크(pre add) : {add}")
        
        add = int(''.join(add)) #리스트형태였던걸 하나로 묶어줌.
        
        #print(f"중간체크(post add) : {add}")
        
        res.append([add, prev])
        #print(f"pre res : {res}")
        
    
    #print(f"post res : {res}")
    res = sorted(res, reverse = True) #이거가 된다는 것도 중요! 리스트안에 리스트도 정렬 가능
    
    return str(int(''.join(unit[1] for unit in res)))



###파이써닉한 모범답안###

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
