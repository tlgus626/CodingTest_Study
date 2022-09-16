def solution(word):
    from itertools import product
    alpha = ['A', 'E', 'I', 'O', 'U']
    a = []
    for i in range(1, 6):
        for j in product(alpha, repeat = i):
            a.append(''.join(list(j)))
    
    return(sorted(a).index(word) + 1)