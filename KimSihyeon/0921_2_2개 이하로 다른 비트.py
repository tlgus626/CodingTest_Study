# Strategies
## 1. 2**23 < 10**15 < 2**64 : Transform given number(N) from digits to 64 bits.
## 2. There are two ways to make larger number than N. (fill '1', swap '0' and '1')

def fill1(n):
    bit = list(format(n, 'b').rjust(64, '0'))
    for i in range(len(bit) - 1, -1, -1):
        if bit[i] == '0':
            bit[i] = '1'
            break
    return int(''.join(bit), 2)


def swap(n):
    bit = list(format(n, 'b').rjust(64, '0'))
    for i in range(len(bit) - 1, -1, -1):
        if bit[i] == '1' and bit[i - 1] == '0':
            bit[i], bit[i - 1] = bit[i - 1], bit[i]
            break
    return int(''.join(bit), 2)


def solution(numbers):
    answer = []
    for n in numbers:
        MIN = min(fill1(n), swap(n))
        MAX = max(fill1(n), swap(n))
        if MIN <= n:
            answer.append(MAX)
        else:
            answer.append(MIN)
    return answer
