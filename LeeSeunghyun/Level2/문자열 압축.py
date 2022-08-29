def solution(s):
    answer = len(s)
    
    # 완전 탐색
    for step in range(1, len(s)//2+1):
        count = 1 # count 변수 사용
        compressed = 0 # 길이만 담는 변수 설정
        prev = s[:step]
        
        for start in range(step, len(s)+step, step):
            
            curr = s[start:start+step]
            
            if curr == prev:
                
                count += 1 # 문자열 대신 count만 증가
            
            else:
                
                compressed += len(str(count)+prev) if count > 1 else len(prev)
                count = 1 # 배열 대신 count = 1로 리셋
                prev = curr
        
        answer = min(answer, compressed)

    return answer
