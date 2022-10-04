def solution(s):
    
    def convert(s, z, r):
        
        # 0제거 후 길이
        ch = bin(s.count("1"))[2:]
        
        # z: 회전 수, r: 0 제거 개수 
        return [z,r+s.count("0")] if ch == s else convert(ch, z+1, r+s.count("0"))
    
    return convert(s, 0, 0)
