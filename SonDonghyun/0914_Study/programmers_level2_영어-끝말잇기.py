def solution(n, words):
    temp = ''
    check_word = []

    for i, word in enumerate(words):
        if i != 0:
            if word[0] != temp[-1] or word in check_word:
                a, b = divmod(i, n)
                return [b + 1, a + 1]
            
            else:
                temp = word
                check_word.append(word)
        else:
            temp = word
            check_word.append(word)

    return [0, 0]