def solution(s):
    result = [0] * 2
    while s != '1':
        result[0] += 1
        result[1] += s.count('0')
        s = bin(s.count('1'))[2:]
    
    return result