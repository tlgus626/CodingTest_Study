def solution(n, words):
    for i, j in enumerate(zip(words[:-1],words[1:])):
        # 두 단어씩 짝지어서 앞 단어의 뒷글자와 뒷 단어의 앞글자가 다르거나 앞에서 한번 더 언급되면 번째 사람과, 몇바퀴째 걸렸는지 출력
        if not j[0][-1]==j[1][0] or not words[:i+2].count(j[1]) == 1:
            p, q = divmod(i+1,n)
            return [q+1,p+1]
    return [0,0]
