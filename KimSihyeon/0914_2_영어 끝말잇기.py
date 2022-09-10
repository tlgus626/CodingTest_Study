def solution(n, words):
    for i in range(1, len(words)):
        # condition 1 : fail to connect string
        # condition 2 : duplicated word
        if words[i][0] != words[i - 1][-1] or any(words[i] == w for w in words[:i - 1]):
            break
            # after 'quotient' rounds, break at 'remain' order
            return [i % n + 1, i // n + 1]
    else:
        return [0, 0]
