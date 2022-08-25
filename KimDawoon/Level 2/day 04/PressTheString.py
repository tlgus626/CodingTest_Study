def solution(s):
    
    # 길이가 1인 문자열은 단순하게 1로 출력
    if len(s) == 1:
            return 1
    
    # 문자와 원하는 슬라이싱 숫자를 넣으면 문자열의 길이를 출력해주는 함수 생성
    def slicestring(lst, k): 
        
        # 글자수대로 분리, 남는 글자는 남는 글자대로 붙음
        ls = [lst[i:i+k] for i in range(0, len(lst), k)]
        
        # 자른 변수 중 맨 앞에 오는 변수 저장
        kkang = [ls[0]]
        
        # 반복 횟수 저장
        tong = [1]
        
        # 다음 올 단어가 이전 단어랑 같으면 +1 다르면 새로이 저장
        for i, j in zip(ls[1:],ls[:-1]):
            if i == j:
                tong[-1] = tong[-1] + 1
            else:
                kkang += [i]
                tong += [1]
        
        # 새로 만든 문자열의 길이를 반환
        return len(''.join([str(z)+t if z > 1 else t for t, z in zip(kkang,tong)]))
    
    # 1개부터 전체 길이의 1/2보다 크지 않은 정수까지만 비교해서 최소 숫자 출력
    return min([slicestring(s, c) for c in range(1,len(s)//1)])
