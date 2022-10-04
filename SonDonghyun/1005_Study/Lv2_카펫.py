def solution(brown, yellow):
    y = [i for i in range(1, yellow + 1) if yellow % i == 0]
    for i in y:
        h, w = i, yellow // i
        if (h + w) * 2 + 4 == brown and h >= w:
            return [h + 2, w + 2]