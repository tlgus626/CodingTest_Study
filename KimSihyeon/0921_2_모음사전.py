def seq_sum(x):
    return (5 ** x - 1) / (5 - 1)


def solution(word):
    v = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    for i, w in enumerate(word):
        answer += 1 + seq_sum(5 - i) * v.index(w)
    return answer
