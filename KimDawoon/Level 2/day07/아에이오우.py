# 설명은 참조
def solution(word):
    
    k = 0
    score = [781, 156, 31, 6, 1]
    dic = {'A':0, 'E':1, 'I':2, "O":3, "U":4}
    for num, c in enumerate(word):
        k += score[num] * dic[c] + 1

    return k
