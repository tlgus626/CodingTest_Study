def solution(s):
    # 문자열 + 부호를 list로 받아드림
    b = list(map(int,s.split(' ')))
    
    # 최대와 최소를 문자열로 다시 출력
    return str(min(b))+' '+str(max(b))
