# from decimal to Kth number
def kth_number(n, k):
    res = ''
    while n > 0:
        res += str(n % k)
        n //= k
    return res[::-1]

# is 'n' prime number?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


def solution(n, k):
    # split string by seperator '0' -> prime candidates
    res = kth_number(n, k).split('0')
    cnt = 0
    for r in res:
        if r.isdigit() and is_prime(int(r)):
            cnt += 1
    return cnt
