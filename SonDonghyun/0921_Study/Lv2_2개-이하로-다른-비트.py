def wow(n):
    a = bin(n)[2:].zfill(len(bin(n)[2:]) + 1)
    if a[-1] == '0':
        result = a[:-1] + '1'
    else:
        result = a[:a.rfind('0')] + '10' + a[a.rfind('0') + 2:]
    return int(result, 2)

def solution(numbers):
    return list(map(wow, numbers))