N = int(input())
A = list(map(int, input().split()))
PLUS, MINUS, PROD, DIVIDE = map(int, input().split())

def calculation(x, y, o) :
    if o == '+' :
        return x + y
    if o == '-' :
        return x - y
    if o == '*' :
        return x * y
    if o == '/' :
        if x < 0 :
            return -1 * ((-1*x)//y)
        else :
            return x//y

MAX = -1*1e9
MIN = 1e9

def DFS(plus, minus, prod, divide, level, now) :
    global MAX, MIN
    if level == N-1 :
        if now > MAX :
            MAX = now
        if now < MIN :
            MIN = now
    else :
        if plus > 0 :
            DFS(plus-1, minus, prod, divide, level+1, calculation(now, A[level+1], '+'))
        if minus > 0 :
            DFS(plus, minus-1, prod, divide, level+1, calculation(now, A[level+1], '-'))
        if prod > 0 :
            DFS(plus, minus, prod-1, divide, level+1, calculation(now, A[level+1], '*'))
        if divide > 0 :
            DFS(plus, minus, prod, divide-1, level+1, calculation(now, A[level+1], '/'))

DFS(PLUS, MINUS, PROD, DIVIDE, 0, A[0])

print(MAX)
print(MIN)
