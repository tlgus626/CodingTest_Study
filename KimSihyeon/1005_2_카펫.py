def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0 and i >= yellow // i:
            if i * 2 + (yellow // i) * 2 + 4 == brown:
                return [i + 2, (yellow // i) + 2]
