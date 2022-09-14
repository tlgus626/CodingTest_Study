def solution(n, lost, reserve):

    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)

    for num in reserve:
        if num - 1 in lost:
            lost = lost - {num - 1}
        elif num + 1 in lost:
            lost = lost - {num + 1}
    
    return n - len(lost) # 위 코드에서 여기만 수정함