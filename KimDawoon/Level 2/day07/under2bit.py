def solution(numbers):
    
    print((62 ^ (62+1)) >> 2)
    
    def findnum(s):
        
        # 전부 1이면 맨 앞쪽에서 비트 체인지
        if all(c == "1" for c in s):
            return "10" + s[:-1]
        
        # 수를 뒤집기
        s = s[::-1]
        for i in range(len(s)):
            
            # 처음이 0이면 1로 바꾸고 끝
            if i == 0 and s[i] == "0":
                s = "1" + s[1:]
                break
            
            # 앞이 1이면서 뒤가 0이면 서로 자리 체인지
            elif s[i] == "0" and s[i-1] == "1":
                s = s[:i-1] + "01" + s[i+1:]
                break
        
        # 뒤집은 수 원상태로 복귀
        return s[::-1]
    
    # 모든 numbers에 적용하기
    return list(map(lambda x: int(findnum(bin(x)[2:]),2), numbers))
