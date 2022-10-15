from math import log2


def solution(n, a, b):
    rounds = [[0, 0] for _ in range(int(log2(n)))]
    if (a + 1) // 2 == (b + 1) // 2:
        return 1
    else:
        # initialize
        rounds[0][0], rounds[0][1] = (a + 1) // 2, (b + 1) // 2
        cnt = 1
        # let's game!
        for i in range(1, len(rounds)):
            cnt += 1
            rounds[i][0] = (rounds[i - 1][0] + 1) // 2
            rounds[i][1] = (rounds[i - 1][1] + 1) // 2
            if rounds[i][0] == rounds[i][1]:
                break
        return cnt
