def solution(s):
    
    # 개수 다르면 False
    if s.count('(') != s.count(')'):
        return False
    
    # 각각 개수가 맞으면서, 괄호열림이 닫힘보다 많거나 같아야함
    opened = 0
    closed = 0
    for i in s:
        if i == '(':
            opened += 1
        else:
            closed += 1
        
        if opened < closed:
            return False
        
    return True
