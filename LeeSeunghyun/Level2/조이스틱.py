#ㅅㅍ 모르겠다 뭔데이거
#내 코드 아니고 모범코드 가져옴

def solution(name):
    answer = 0
    min_move = len(name) -1
    for i in range(len(name)):
        answer += min(ord(name[i])-ord("A"),ord("Z")+1-ord(name[i]))
    
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    answer += min_move
    
    return answer
