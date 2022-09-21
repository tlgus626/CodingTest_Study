### 시간효율성 못 줄여서 답 봄
def solution(prices):
    a = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                break
        a.append(j - i)
    return a